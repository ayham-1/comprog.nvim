#!/bin/python3

import subprocess
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
        args = "{} {}".format(file_loc, self.args)
        output = subprocess.check_output("{} {}".format(self.cmd, args),
                                         shell=True)

    def run(self):
        cprog = os.path.join(xdg_cache_home(), "comprog", "cprog")
        output = subprocess.check_output("exec {}".format(cprog),
                                         shell=True)
        return output

if __name__ == "__main__":
    import os
    os.system("mkdir -p {}".format(os.path.join(xdg_cache_home(), "comprog")))
    cpp = Cplusplus()
    cpp.compile("../../test/main.cpp")
    print(cpp.run())
