#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dev script to setup a test database. """

import sqlite3 as lite
import time
import util

with lite.connect('People.db') as con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS People")
    cur.execute(
        "CREATE TABLE People(Id INTEGER PRIMARY KEY AUTOINCREMENT, blipId INTEGER, Nick TEXT, isHere INTEGER," +
        "totalTime FLOAT, lastLogin FLOAT)"
    )

    rfId = util.encode("2016050010")
    nick_temp = 'Dalsmo'
    cur.execute("INSERT INTO People (blipId, Nick, isHere, totalTime, lastLogin) VALUES (?,?,?,?,?);",
                (rfId, nick_temp, 1, 0, time.time()))
