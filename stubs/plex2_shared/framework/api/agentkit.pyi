# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from ..objects import MediaContainer

from .base import BaseKit

class MediaContentsDirectory:
    def __init__(self, core, path, readonly=True): ...
    def __contains__(self, item): ...
    def __getitem__(self, item): ...
    def __setitem__(self, item, data): ...

class MediaStream:
    def __init__(self, core, el): ...

class MediaPart:
    streams: List[MediaStream]
    thumbs: Union[MediaContentsDirectory]
    art: Union[MediaContentsDirectory]
    subtitles: Union[MediaContentsDirectory]
    def __init__(self, core, el): ...

class Setting(object):
    id: Any
    value: Any
    def __init__(self, core, el): ...

class MediaItem(object):
    parts: List[MediaPart]
    def __init__(self, core, el): ...

class MediaDict(dict):
    def __contains__(self, item) -> bool: ...
    def __getitem__(self, item) -> Any: ...

class MediaTree:
    items: List[MediaItem]
    settings: Dict[Any, Setting]
    children: List[MediaTree]

    def all_parts(self) -> List[MediaPart]:
        """ Return an array of all parts owned by this item and its' sub-items """

class MediaObject:
    """
    A MediaObject represents a media item discovered by PMS and encapsulates any information provided by the server.

    It is intended to provide hints to metadata agents when finding metadata to download.
    """
    primary_agent: Any
    primary_metadata: Any
    filename: Any
    guid: Any
    parent_metadata: Any
    tree: Any
    id: Any
    hash: Any
    originally_available_at: Any

class Media:
    @classmethod
    def TreeForDatabaseID(cls, dbid, level_names=[],
                          host='127.0.0.1', parent_id=None, level_attribute_keys=[]) -> MediaTree:
        ...

    class Movie(MediaObject):
        primary_metadata: Any
        name: Any
        openSubtitlesHash: Any
        year: Any
        duration: Any

    class TV_Show(MediaObject):
        show: Any
        season: Any
        episode: Any
        name: Any
        openSubtitlesHash: Any
        year: Any
        duration: Any
        episodic: Any

    class Album(MediaObject):
        name: Any
        artist: Any
        album: Any
        track: Any
        index: Any
        parentGUID = None

    class Artist(MediaObject):
        artist: Any
        album: Any
        track: Any
        index: Any

    class PhotoAlbum(MediaObject): ...
    class Photo(MediaObject): ...

TMedia = TypeVar('TMedia')

class BaseAgent(Generic[TMedia]):
    name: str
    languages: List[str]
    primary_provider: bool
    contributes_to: List[str]
    accepts_from: List[str]
    fallback_agent: Any
    persist_stored_files: bool
    version: int

    def search(self, results: MediaContainer, media: TMedia, lang: Any, *,
               tree: MediaTree, manual: bool, primary: bool):
        '''
        Functions that agents should implement.

        all kwargs are optional like overload.
        '''
        ...

    def update(self, metadata, media: MediaTree, lang: Any, *,
               force, child_guid, child_id, periodic, prefs: dict):
        '''
        Functions that agents should implement.

        all kwargs are optional like overload.
        '''
        ...

class TV_Shows(BaseAgent[Media.TV_Show]):
    ...

class Movies(BaseAgent):
    ...

class Artist(BaseAgent):
    ...

class Album(BaseAgent):
    ...

class Photos(BaseAgent):
    ...

class AgentKit(BaseKit):
    '''
    The AgentKit API class handles commmunication between plug-ins and the agent service,
    responding to incoming requests and forwarding them to custom Agent classes as appropriate.
    '''

    def __init__(self):
        self.TV_Shows = TV_Shows
        self.Movies = Movies
        self.Artist = Artist
        self.Album = Album
        self.Photos = Photos

Agent: AgentKit
