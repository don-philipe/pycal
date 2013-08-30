#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Configurator import *

class Calendar:
    """
    """

    def __init__(self, configfile = "./pycal.conf"):
        """
        @param configfile:
        """
        self.configurator = Configurator(configfile)
