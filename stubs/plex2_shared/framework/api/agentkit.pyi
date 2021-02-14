# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from .base import BaseKit

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
