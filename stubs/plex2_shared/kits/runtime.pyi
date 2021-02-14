# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from .base import BaseKit

def handler(prefix, name, thumb=None, art=None, titleBar=None, share=False, allow_sync=False):
    pass

class PluginKit(BaseKit):
    @property
    def Identifier(self) -> str:
        '''
        A read-only attribute containing the identifier of the plug-in.
        '''
        ...

    @property
    def Title(self) -> str:
        '''
        A read-only attribute containing the plug-in's title.
        '''
        ...

    @property
    def IconResourceName(self) -> str:
        '''
        A read-only attribute containing the name of the plug-in's icon image resource file.
        '''
        ...

    @property
    def ArtResourceName(self) -> str:
        '''
        A read-only attribute containing the name of the plug-in's background art image resource file.
        '''
        ...

    # TODO:  more properties
    # TODO: export api from ._init
Plugin: PluginKit

class ClientKit(BaseKit):
    ...
    # TODO: export api from ._init
Client: ClientKit

class PlatformKit(BaseKit):
    @property
    def OS(self) -> str:
        '''
        Reports the current server's operating system.

        :returns: The current platform; either `MacOSX`, `Windows` or `Linux`.
        '''

    @property
    def OSVersion(self) -> str:
        '''
        Reports the current server's operating system version.

        :returns: The version of the current platform, e.g. `10.7.0`
        '''

    @property
    def CPU(self) -> str:
        '''
        Reports the current server's CPU architecture.

        :returns: The current CPU architecture; either `i386`, `MIPS`, `mips64` or `armv5tel`.
        '''

    @property
    def MachineIdentifier(self) -> str:
        '''
        Reports the current server's machine identifier.

        :returns: The unique identifier for the server.
        '''

    @property
    def ServerVersion(self) -> str:
        '''
        Reports the current server's version string.

        :returns: The version the server.
        '''
    # TODO: export api from ._init
Platform: PlatformKit

class RouteKit(BaseKit):
    ...
    # TODO: export api from ._init
Route: RouteKit

class RequestKit(BaseKit):
    ...
    # TODO: export api from ._init
Request: RequestKit

class ResponseKit(BaseKit):
    ...
    # TODO: export api from ._init
Response: ResponseKit

class PrefsKit(BaseKit):
    def __getitem__(self, name):
        ...
    ...
    # TODO: export api from ._init
Prefs: PrefsKit

class RuntimeKit(BaseKit):
    ...
    # TODO: export api from ._init
