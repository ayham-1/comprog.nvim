#!/bin/python3

import subprocess

from data_types import Language

class Python(Language):
    def __init__(self):
        self.name = "Python"
        self.ext = [".py",]
        self.cmd = "python"

    def run(self, file_loc, stdin_input):
        args = "{}".format(file_loc)
        output = subprocess.check_output("echo {} | python {}".format(stdin_input, file_loc),
                       shell=True)
        return output

if __name__ == "__main__":
    import os
    from xdg import (xdg_cache_home)
    os.system("mkdir -p {}".format(os.path.join(xdg_cache_home(), "comprog")))
    py = Python()
    print(py.run("../../test/main.py", "ello, there!"))
