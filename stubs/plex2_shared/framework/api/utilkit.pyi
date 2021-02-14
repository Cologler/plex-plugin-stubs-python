# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import datetime
import re

from .base import BaseKit

class AMFKit(BaseKit):
    ... # TODO

class HashKit(BaseKit):
    def MD5(self, data, digest=False) -> str: ...
    def SHA1(self, data, digest=False) -> str: ...
    def SHA224(self, data, digest=False) -> str: ...
    def SHA256(self, data, digest=False) -> str: ...
    def SHA384(self, data, digest=False) -> str: ...
    def SHA512(self, data, digest=False) -> str: ...
    def CRC32(self, data) -> str: ...

class RegexKit(BaseKit):
    IGNORECASE = re.IGNORECASE
    MULTILINE = re.MULTILINE
    DOTALL = re.DOTALL
    def __call__(self, pattern: AnyStr, flags=0) -> re.Pattern: ...

class StringKit(BaseKit):
    ... # TODO

class DatetimeKit(BaseKit):
    def Now(self) -> datetime.datetime: ...
    def UTCNow(self) -> datetime.datetime: ...
    def ParseDate(self, date: str, fmt=None) -> Optional[datetime.datetime]: ...
    def Delta(self, **kwargs) -> datetime.timedelta: ...
    def TimestampFromDatetime(self, dt: datetime.datetime) -> int:
        """
        Converts the given *datetime* object to a UNIX timestamp.
        """
    def FromTimestamp(self, ts: float) -> datetime.datetime:
        """
        Converts the given UNIX timestamp to a *datetime* object.
        """
    def MillisecondsFromString(self, s: str) -> int: ...

class UtilKit(BaseKit):
    def Floor(self, x: SupportsFloat) -> int: ...
    def Ceiling(self, x: SupportsFloat) -> int: ...
    def VersionAtLeast(self, version_string, *components): ...
    def ListSortedByKey(self, l, key) -> list: ...
    def ListSortedByAttr(self, l, attr) -> list: ...
    def SortListByKey(self, l, key): ...
    def SortListByAttr(self, l, attr): ...
    def LevenshteinDistance(self, first, second): ...
    def LongestCommonSubstring(self, first, second): ...
    def Random(self) -> float:
        """
        Returns a random number between 0 and 1.
        """
    def RandomInt(self, a: int, b: int) -> int:
        """
        Returns a random integer *N* such that `a <= N <= b.
        """
    def RandomItemFromList(self, l: list) -> Any: ...
    def RandomChoice(self, l: Sequence) -> Any: ...
    def RandomSample(self, l, count): ...

Util = UtilKit()

# UtilKit._init
AMF: AMFKit
Hash: HashKit
String: StringKit
Datetime: DatetimeKit
Archive: ArchiveKit
Regex: RegexKit
E = StringKit.Encode
D = StringKit.Decode
