#!/bin/python3

import pynvim

@pynvim.plugin
class Main(object):
    config = None

    def __init__(self, vim):
        self.vim = vim

    @pynvim.command('ComprogStartUp', nargs='*')
    def startUp(self, args):
        pass

    @pynvim.command('ComprogTaskCreate', nargs='*')
    def createTask(self, args):
        pass

    @pynvim.command('ComprogTaskLoad', nargs='*')
    def loadTask(self, args):
        pass

    @pynvim.command('ComprogTaskDel', nargs='*')
    def delTask(self, args):
        pass

    @pynvim.command('ComprogTaskEdit', nargs='*')
    def editTask(self, args):
        pass

    @pynvim.command('ComprogTaskLoadInput', nargs='*')
    def loadInputTask(self, args):
        pass

    @pynvim.command('ComprogTaskCompile', nargs='*')
    def compileTask(self, args):
        pass

    @pynvim.command('ComprogTaskRun', nargs='*')
    def runTask(self, args):
        pass
