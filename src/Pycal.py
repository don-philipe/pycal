#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Pycal:
    """
    The entry class for the pycal program.
    """

    def __init__(self, interval, db, calendars):
        """
        @param interval: the interval a backup of all calendars will
        be made, in days (integer)
        @param db: the database which will be used for the calendar
        (locally), must be a string
        @param calendars: a list of calendars
        """
        self.__backupinterval = interval
        if(db == "sqlite"):
            self.__database = "sqlite"
        else:
            print "no other databases supported right now"
        self.__calendar_list = calendars

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
