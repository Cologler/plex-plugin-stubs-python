# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .base import BaseKit

class BaseHTTPKit(BaseKit):
    ...

class XMLRPCKit(BaseKit):
    ...

class HTTPKit(BaseHTTPKit):
    ... # TODO

class NetworkKit(BaseKit):
    ... # TODO
Network: NetworkKit

# NetworkKit._children
HTTP:  HTTPKit
XMLRPC: XMLRPCKit
