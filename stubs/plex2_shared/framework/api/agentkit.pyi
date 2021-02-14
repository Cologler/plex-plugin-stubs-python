# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from .base import BaseKit

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
    def TreeForDatabaseID(cls, dbid, level_names=[], host='127.0.0.1', parent_id=None, level_attribute_keys=[]):
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


class BaseAgent:
    name: str
    languages: List[str]
    primary_provider: bool
    contributes_to: List[str]
    accepts_from: List[str]
    fallback_agent: Any
    persist_stored_files: bool
    version: int

    def search(self, media, lang):
        '''
        Functions that agents should implement
        '''
        ...

    def update(self, metadata, media, lang):
        '''
        Functions that agents should implement
        '''
        ...

class TV_Shows(BaseAgent):
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
