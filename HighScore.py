#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import requests
import os
import time
import lights


while True:
    os.system('clear')
    con = lite.connect('People.db')
    con.row_factory = lite.Row

    with con:
        cur = con.cursor()

        print("------------ Highscore -----------")

        cur.execute("SELECT * FROM People ORDER BY totalTime DESC")
        rows = cur.fetchall()

        for i, row in enumerate(rows):
            print('{position}: {nick:10} score: {score}'.format(position=i+1, nick=row['Nick'], score=row['totalTime']))

        print("------------- People online ------")

        cur.execute("SELECT * FROM People WHERE isHere = 1")
        rows = cur.fetchall()
        
        # display som people
        for row in rows:
            print(row['Nick'].ljust(10))
        
        # prata med dorropnare och be dem tana
        if rows:
            lights.on()
        else:
            lights.off()


    time.sleep(3)
