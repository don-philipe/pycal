#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Calendar:
    """
    Represents a single calendar.
    """

    __name = "default-calendar"
    __address = "./local.sqlite"
    __remote = False
    __refresh = 30   # in min
    __readonly = False

    def __init__(self, name, address, remote, refresh, readonly):
        """
        @param name: a string
        @param address: the address is either local address in the
        filesystem or an url
        @param remote: a boolean which defines if address is a local
        or remote one
        @param refresh: an integer which indicates how many seconds
        to wait between two refreshes
        @param readonly: a boolean which defines if one can write
        the calendar or not
        """
        self.__name = name
        self.__address = address
        self.__remote = remote
        self.__refresh = refresh
        self.__readonly = readonly

    def getName(self):
        """
        @return: calendars name
        """
        return self.__name
