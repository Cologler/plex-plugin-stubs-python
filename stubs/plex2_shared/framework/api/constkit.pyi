# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from ... import ConstantGroup

class ClientPlatforms(ConstantGroup):
    MacOSX: str
    Linux: str
    Windows: str
    iOS: str
    Android: str
    LGTV: str
    Roku: str
ClientPlatform: ClientPlatforms

# TODO: more ConstantGroups

# ConstKit._init
CACHE_1MINUTE: int
CACHE_1HOUR: int
CACHE_1DAY: int
CACHE_1WEEK: int
CACHE_1MONTH: int
# TODO: ConstKit._init::OldProtocols
