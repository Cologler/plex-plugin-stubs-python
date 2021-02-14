# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .base import BaseKit

class HelperKit(BaseKit):
    '''
    Executes and interacts with external binaries.
    '''
    def Run(self, helper: str, *args):
        '''
        Runs a helper and returns any output.
        '''

Helper: HelperKit
