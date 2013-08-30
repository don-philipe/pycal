#!/usr/bin/env python
#-*- coding:utf-8 -*-

import ConfigParser

class Configurator:
    """
    """

    def __init__(self, configfile):
        """
        @param configfile: full path of the configurationfile
        """
        self.configfile = configfile
        self.parser = ConfigParser.SafeConfigParser()
        self.parser.read(configfile)
        # for testing:
        print self.parser.sections()

    def addCalendar(name, address, refresh, readonly):
        """
        Adds a calendar to the configuration file.
        @param name: name of the calendar
        @param address: remote address
        @param refresh: refresh rate
        @param readonly: must be a boolean value
        """
        self.parser.add_section(name)
        self.parser.set(name, 'address', address)
        self.parser.set(name, 'refresh', refresh)
        self.parser.set(name, 'readonly', readonly)
        self.parser.write()
        with open(self.configfile, 'wb') as config_file:
            self.parser.write(config_file)

