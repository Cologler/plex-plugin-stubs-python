# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *

from ..components.localization import LocalString, LocalStringFormatter

from .base import BaseKit

class LocaleKit(BaseKit):
    Language: str
    CountryCodes: str
    DefaultLocale: str

    @property
    def Geolocation(self) -> str:
        """
        Returns the user's country, obtained via IP-based geolocation, e.g. ``US``.
        """

    @property
    def CurrentLocale(self) -> str:
        """
        Returns the locale of the user currently making a request to the plug-in, or *None* if no locale was provided.
        """

    def LocalString(self, key: str) -> LocalString:
        """
        Retrieves the localized version of a string with the given key. Strings from the user's
        current locale are given highest priority, followed by strings from the default locale.

        See `String files` for more information on proividing localized versions of strings.
        """

    def LocalStringWithFormat(self, key, *args) -> LocalStringFormatter:
        """
        Retrieves the localized version of a string with the given key, and formats it using the
        given arguments.
        """

Locale: LocaleKit

# LocaleKit._init
def L(key: str) -> str:
    '''
    same as `Locale.LocalString()`
    '''

def F(key: str) -> str:
    '''
    same as `Locale.LocalStringWithFormat()`
    '''
