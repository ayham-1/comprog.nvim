#!/bin/python3

from data_types import Supplier

import os
import zipfile
from xdg import (xdg_cache_home,
                 xdg_config_home)

class Hackerrank(Supplier):
    def __init__(self):
        self.url = "hackerrank.com"
        self.name = "HackerRank"

    def getProblemSample(self, name):
        problem_url = ("https://www.hackerrank.com/rest/contests/" \
            "master/challenges/{}/download_testcases").format(name)

        # Download sample data then extract
        destination = os.path.join(xdg_cache_home(), "comporg")
        os.system("wget -O {} {}".format("sample.zip", problem_url))
        os.system("mkdir -p {}".format(destination))
        os.system("mv sample.zip {}".format(destination))
        sample_file_zip = os.path.join(destination, "sample.zip")
        with zipfile.ZipFile(sample_file_zip, 'r') as zip_ref:
            zip_ref.extractall(destination)

        # Read sample input
        input_data = []
        inputs = os.listdir(os.path.join(destination, "input"))
        for i in inputs:
            f = open(os.path.join(destination, "input", i))
            input_data.append(f.read())

        # Read sample output
        output_data = []
        outputs = os.listdir(os.path.join(destination, "output"))
        for i in outputs:
            f = open(os.path.join(destination, "output", i))
            output_data.append(f.read())

        return input_data, output_data
        
if __name__ == "__main__":
    hr = Hackerrank()

    print(hr.getProblemSample("new-year-chaos"))
