#!/bin/python3

import pynvim

@pynvim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.command('ComprogCreateTask', nargs='*')
    def createTask(self, args):
        self.vim.command('echo "{}"'.format(args[0]))

    @pynvim.command('DoItPython')
    def doItPython(self):
        self.vim.command('echo "ello"')
