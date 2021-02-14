# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .base import BaseKit
from .networkkit import BaseHTTPKit

class PlistKit(BaseHTTPKit):
    ... # TODO

class JSONKit(BaseHTTPKit):
    ... # TODO

class RSSKit(BaseHTTPKit):
    ... # TODO

class YAMLKit(BaseHTTPKit):
    ... # TODO

class XMLKit(BaseHTTPKit):
    ... # TODO

class HTMLKit(BaseHTTPKit):
    ... # TODO

class ParseKit(BaseHTTPKit):
    ... # TODO

# ParseKit._init
JSON: JSONKit
Plist: PlistKit
RSS: RSSKit
YAML: YAMLKit
XML: XMLKit
HTML: HTMLKit
