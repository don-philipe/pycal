#!/usr/bin/env python
#-*- coding:utf-8 -*-

import ConfigParser
import Calendar
import Pycal


class Configurator:
    """
    Reads the configuration from file and adjusts the program and calendars.
    """

    def __init__(self, configfile):
        """
        Reads the configfile.
        @param configfile: full path of the configurationfile
        """
        self.configfile = configfile
        self.config_parser = ConfigParser.SafeConfigParser()
        self.config_parser.read(configfile)

    def configure(self):
        """
        Configures the program and the calendars.
        @return: a pycal-instance
        """
        calendar_list = []
        for section in self.config_parser.sections():
            if section == "pycal":
                interval = self.config_parser.getint("pycal", "backup")
                db = self.config_parser.get("pycal", "database")
            else:
                calendar_list.append(self.__configureCalendar(section))
        return Pycal.Pycal(interval, db, calendar_list)

    def __configureCalendar(self, section):
        """
        @param section: the calendar which will be configured here
        @return: a configured (initialized) Calendar
        """
        name = self.config_parser.get(section, "name")
        address = self.config_parser.get(section, "address")
        remote = self.config_parser.getboolean(section, "remote")
        refresh = self.config_parser.getint(section, "refresh")
        readonly = self.config_parser.getboolean(section, "readonly")
        return Calendar.Calendar(name, address, remote, refresh, readonly)

    def addCalendarsection(self, name, address, refresh, readonly, remote):
        """
        Adds a calendar to the configuration file.
        @param name: name of the calendar
        @param address: remote address
        @param refresh: refresh rate
        @param readonly: must be a boolean value
        """
        self.config_parser.add_section(name)
        self.config_parser.set(name, 'address', address)
        self.config_parser.set(name, 'refresh', refresh)
        self.config_parser.set(name, 'readonly', readonly)
        self.config_parser.set(name, 'remote', remote)
        self.config_parser.write()
        with open(self.configfile, 'wb') as config_file:
            self.config_parser.write(config_file)

    #TODO (later)
    def validateConfigurationFile(self):
        """
        Validates the configuration file.
        Will be implemented later, this is only a reminder.
        """
        pass

    def getNumberOfSections(self):
        """
        @return: number of sections in configurationfile
        """
        return self.config_parser.sections().length
