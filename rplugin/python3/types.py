#!/bin/python3

class Supplier:
    url = ""
    name = ""
    
    def __init__(self, url, name):
        self.url = url
        self.name = name

class Language:
    name = ""
    ext = ""
    cmd = ""
    args = ""

    def __init__(self, name, ext, cmd, args):
        self.name = name
        self.ext = ext
        self.cmd = cmd
        self.args = args

    def compile(self, args):
        self.args = args
        pass

    def run(self, args, stdin):
        pass

class Task:
    pwd = ""
    name = ""
    lang = None
    supplier = None
    file_loc = ""

    def __init__(self, name, lang, supplier, file_loc, pwd):
        self.name = name
        self.lang = lang
        self.supplier = supplier
        self.file_loc = file_loc
        self.pwd = pwd

    def setName(self, name):
        self.name = name

    def setLang(self, lang):
        self.lang = lang

    def setFileLoc(self, loc):
        self.file_loc = loc

class Config:
    pwd = ""
    tasks = []

    def __init__(self)
        pass
    
    def load(self, config):
        pass

