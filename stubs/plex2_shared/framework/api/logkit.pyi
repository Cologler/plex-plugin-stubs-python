# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .base import BaseKit

class LogKit(BaseKit):
    def Debug (self, fmt, *args, **kwargs): ...
    def Info  (self, fmt, *args, **kwargs): ...
    def Warn  (self, fmt, *args, **kwargs): ...
    def Error (self, fmt, *args, **kwargs): ...
    def Critical(self, fmt, *args, **kwargs): ...
    def Exception(self, fmt, *args, **kwargs):
        '''
        The same as the *Critical* method above,
        but appends the current stack trace to the log message.

        note:: This method should only be called when handling an exception.
        '''
    def Stack(self): ...
    def __call__(self, fmt, *args, **kwargs):
        '''as same as call `.Info()`.'''
Log: LogKit
