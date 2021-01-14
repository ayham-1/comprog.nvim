#!/bin/python3

import os
import subprocess
from xdg import (xdg_cache_home)

from data_types import Language

class Clang(Language):
    def __init__(self):
        self.name = "C"
        self.ext = [".c"]
        self.cmd = "cc"
        self.args = "-o {}".format(os.path.join(xdg_cache_home(), "comprog",
                                                "cprog"))

    def compile(self, file_loc):
        args = "{} {}".format(self.args, file_loc)
        output = subprocess.check_output("{} {}".format(self.cmd, args),
                                         shell=True)
        return output

    def run(self, stdin_input):
        cprog = os.path.join(xdg_cache_home(), "comprog", "cprog")
        output = subprocess.check_output("echo {} | exec {}".format(stdin_input, cprog),
                                         shell=True)
        return output

if __name__ == "__main__":
    os.system("mkdir -p {}".format(os.path.join(xdg_cache_home(), "comprog")))
    c = Clang()
    c.compile("../../test/main.c")
    print(c.run("ello, there!"))
