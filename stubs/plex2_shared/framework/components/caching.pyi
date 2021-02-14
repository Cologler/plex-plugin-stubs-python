# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from ..exceptions import FrameworkException

from .base import BaseComponent

class CacheManager(dict):
    def __setitem__(self, name, value):
        raise FrameworkException("Cache manager items can't be set directly.")
    def trim(self, max_size: int, max_items: int): ...
    def clear(self): ...
    @property
    def item_count(self) -> int: ...

class Caching(BaseComponent):
    caches_path: str
    managers: Dict[str, CacheManager]

    def get_cache_manager(self, name: str, system=False) -> CacheManager:
        ...
