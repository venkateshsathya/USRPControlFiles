#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:43:25 2020

@author: venkatesh
"""

import sys
class Logger(object):
    def __init__(self,logfilename):
        self.terminal = sys.stdout
        self.log = open(logfilename, "a")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  
    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    
