# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

class LocalString:
    def __str__(self) -> str: ...
    def localize(self, locale: Optional[str]) -> str: ...

class LocalStringPair:
    def __str__(self) -> str: ...
    def localize(self, locale: Optional[str]) -> str: ...

class LocalStringFormatter(LocalStringPair):
    ...

