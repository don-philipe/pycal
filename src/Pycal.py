#!/usr/bin/env python
#-*- coding:utf-8 -*-

import Configurator


class Pycal:
    """
    The entry class for the pycal program.
    """

    # holds all calendars configured in the configfile:
    __calendar_list = []
    __backupinterval = 30   # days
    __database = "sqlite"

    def __init__(self, conffile="../pycal.conf"):
        """
        @param conffile: the configurationfile, is optional
        """
        self.configurator = Configurator.Configurator(conffile)
        self.calendar_list = self.configurator.configure(self)

    def run(self):
        """
        Start the real work.
        """
        pass

    def setBackupinterval(self, interval):
        """
        @param interval: the interval a backup of all calendars will
        be made, in days (integer)
        """
        self.__backupinterval = interval

    def setDatabase(self, db):
        """
        @param db: the database which will be used for the calendar
        (locally), must be a string
        """
        if(db == "sqlite"):
            self.__database = "sqlite"
        else:
            print "no other databases supported right now"
