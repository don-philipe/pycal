#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sqlite3


class DBConnector:
    """
    Connects to database and manages db-operations.
    At the moment only supports sqlite
    """

    __db = ""

    #TODO: in-memory db?
    def __init__(self, dbfile):
        """
        @param dbfile: the databasefile
        """
        self.__db = dbfile
        self.__conn = sqlite3.connect(self.__db)

    def newCalendar(self, name):
        """
        Adds a new calendar into the database.
        @param name: the name of the calendar
        """
        c = self.__conn.cursor()
        #TODO:
        c.execute('''CREATE TABLE ?
                             (date_start text, date_end text,
                             comment text)''', name)
        self.__conn.commit()

    def delCalendar(self, name):
        """
        Deletes a calendar from the database.
        @param name: the name of the calendar
        """
        c = self.__conn.cursor()
        c.execute('''DROP TABLE ?''', name)
        self.__conn.commit()

    def closeConnection(self):
        """
        Closes the connection to the database.
        """
        self.__conn.close()

    def reopenConnection(self):
        """
        Reopens the connection to the database.
        """
        self.__conn = sqlite3.connect(self.__db)
