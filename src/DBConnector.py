#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sqlite3


class DBConnector:
    """
    Connects to database and manages db-operations.
    At the moment only supports sqlite
    """

    #TODO: in-memory db necessary?
    def __init__(self, dbfile):
        """
        Opens a connection to the database, or creates
        a new database if none exists.
        @param dbfile: the databasefile
        """
        self.__db = dbfile
        self.__conn = sqlite3.connect(self.__db)
        self.__cursor = self.__conn.cursor()
        try:
            self.__cursor.execute("SELECT * FROM calendars")
        except sqlite3.Error as e:
            if "no such table" in e.args[0]:
                print "missing tables, creating ..."
                self.__createDB()

    def __createDB(self):
        """
        Creates a new Database if none exists and adds the
        tables neccessary.
        """
        #TODO:
        self.__cursor.execute('''CREATE TABLE calendars
                             (cal_id text, cal_name text,
                             description text)''')
        self.__cursor.execute('''CREATE TABLE events
                             (event_id text, cal_id text,
                             event_start integer, event_end integer,
                             title text, description text,
                             alarm_id text)''')
        self.__cursor.execute('''CREATE TABLE alarms
                             (alarm_id text, start integer,
                             last_ack integer)''')
        self.__cursor.execute('''CREATE TABLE todos
                             (todo_id text, cal_id text,
                             title text, description text,
                             alarm_id text)''')
        self.__conn.commit()

    def newCalendar(self, cal_id, cal_name, cal_desc):
        """
        Adds a new calendar into the database.
        @param cal_id:
        @param cal_name: the name of the calendar
        @param cal_desc:
        """
        #TODO:
        self.__cursor.execute('''INSERT INTO calendars
                             VALUES (?, ?, ?)''', cal_id, cal_name, cal_desc)
        self.__conn.commit()

    def delCalendar(self, cal_name):
        """
        Deletes a calendar from the database.
        @param cal_name: the name of the calendar
        """
        c = self.__conn.cursor()
        c.execute('''DELETE FROM calendars
                WHERE cal_name=?''', cal_name)
        self.__conn.commit()

    def changeCalendar(self):
        """
        """
        pass

    def newEvent(self):
        """
        """
        pass

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

    #TODO(later)
    def checkDB(self):
        """
        """
        pass
