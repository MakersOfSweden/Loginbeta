#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dev script to setup a test database. """

import sqlite3 as lite
import time
import hasher

with lite.connect('People.db') as con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS People")
    cur.execute(
        "CREATE TABLE People(Id INT PRIMARY KEY AUTOINCREMENT, blipId INT, Nick TEXT, isHere INT," +
        "totalTime FLOAT, lastLogin FLOAT)"
    )

    rfId = hasher.encode("2016050010")
    nick_temp = 'Dalsmo'
    cur.execute("INSERT INTO People (blipId, Nick, isHere, totalTime, lastLogin) VALUES (?,?,?,?,?,?);",
                (rfId, nick_temp, 1, 0, time.time()))
