#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dev script to change user rfid. """

import sqlite3 as lite
import util
import getpass

dbName = input("Enter db to operate on:")

con = lite.connect(dbName)

with con:
    cur = con.cursor()
    
    oldid = util.encode(getpass.getpass("Enter user old rfid:"))
    newid = util.encode(getpass.getpass("Enter user ned rfid:"))
    
    cur.execute("UPDATE People SET blipId = ? WHERE blipId = ?", (newid, oldid))

