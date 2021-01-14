#!/bin/python3

import os
import subprocess
from xdg import (xdg_cache_home)

from data_types import Language

class Rust(Language):
    def __init__(self):
        self.name = "Rust"
        self.ext = ["rust"]
        self.cmd = "rustc"
        self.args = "-o {}".format(os.path.join(xdg_cache_home(), "comprog",
                                                "rprog"))

    def compile(self, file_loc):
        args = "{} {}".format(self.args, file_loc)
        output = subprocess.check_output("{} {}".format(self.cmd, args),
                                         shell=True)
        return output

    def run(self, stdin_input):
        rprog = os.path.join(xdg_cache_home(), "comprog", "rprog")
        output = subprocess.check_output("echo {} | exec {}".format(stdin_input, rprog), 
                                         shell=True)
        return output

if __name__ == "__main__":
    os.system("mkdir -p {}".format(os.path.join(xdg_cache_home(), "comprog")))
    rs = Rust()
    rs.compile("../../test/main.rs")
    print(rs.run("ello, there!"))
