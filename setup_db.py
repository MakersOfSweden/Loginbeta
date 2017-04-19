#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dev script to setup a test database. """

import sqlite3 as lite
import time
import util

con = lite.connect('People.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS People")
    cur.execute(
        "CREATE TABLE People(Id INT, blipId INT, Nick TEXT, isHere INT," +
        "totalTime FLOAT, lastLogin FLOAT)"
    )

    temp_id = 1
    rfId = util.encode("2016050010")
    nick_temp = 'Dalsmo'
    cur.execute("INSERT INTO People VALUES (?,?,?,?,?,?);",
                (temp_id, rfId, nick_temp, 1, 0, time.time()))
