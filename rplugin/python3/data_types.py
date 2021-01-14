#!/bin/python3

import json

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
    name = ""
    lang = ""
    supplier = ""
    file_loc = ""

    def __init__(self, name, lang, supplier, file_loc):
        self.name = name
        self.lang = lang
        self.supplier = supplier
        self.file_loc = file_loc

    def setName(self, name):
        self.name = name

    def setLang(self, lang):
        self.lang = lang

    def setFileLoc(self, loc):
        self.file_loc = loc

    def serialize(self):
        dat = {
            "name": self.name,
            "lang": self.lang.name,
            "supplier": self.supplier.name,
            "file_loc": self.file_loc,
        }

        return dat

    def deserialize(self, dat):
        parsed = json.loads(dat)
        self.name = parsed["name"]
        self.lang = parsed["lang"]
        self.supplier = parsed["supplier"]
        self.file_loc = parsed["file_loc"]

class Config:
    pwd = ""
    tasks = []

    def __init__(self, file_loc):
        self.pwd = file_loc
        with open(self.pwd) as f:
            config_dat = f.read()
            self.deserialize(config_dat)

    def save(self):
        dat = self.serialize()
        with open(self.pwd) as f:
            json.dump(dat, f, indent=4)

    def serialize(self):
        dat = {
            "pwd": self.pwd,
            "tasks": []
        }

        for task in task:
            dat["tasks"].update(task.serialize())

        return dat

    def deserialize(self, dat):
        parsed = json.loads(dat)
        assert(self.pwd, parsed["pwd"]), "create and load config from the same place!"

        for task in parsed["tasks"]:
            parsed_task = Task()
            parsed_task.deserialize(task)
            tasks.append(parsed_task)
