#!/bin/python3

import os
from xdg import (xdg_cache_home)

from data_types import Language

class Cplusplus(Language):
    def __init__(self):
        self.name = "C++"
        self.ext = ["cpp", "cxx", "c++"]
        self.cmd = "c++"
        self.args = "-o {}".format(os.path.join(xdg_cache_home(), "comprog",
                                                "cprog"))
    
    def compile(self, file_loc):
        args = " {} {}".format(file_loc, self.args)
        os.system("{} {}".format(self.cmd, args))

if __name__ == "__main__":
    os.system("mkdir -p {}".format(os.path.join(xdg_cache_home(), "comprog")))
    cpp = Cplusplus()
    cpp.compile("../../test/main.cpp")
    os.system("{}".format(os.path.join(xdg_cache_home(), "comprog", "cprog")))
