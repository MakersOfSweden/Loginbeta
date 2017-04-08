#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import requests
import os
import time

while True:
    os.system('clear')
    con = lite.connect('People.db')
    with con:
        cur = con.cursor()

        print("------------ Highscore -----------")

        cur.execute("SELECT * FROM People ORDER BY totalTime DESC")
        rows = cur.fetchall()

        for i in range(0, len(rows)):
            print(str(i+1) + ": " + str(rows[i][2]).ljust(10) +
                  " score: " + time.strftime("%H:%M:%S", time.gmtime(rows[i][4])))

        print("------------- People online ------")

        cur.execute("SELECT * FROM People WHERE isHere = 1")
        rows = cur.fetchall()
        
        # display som people
        for row in rows:
            print(str(row[2]).ljust(10))
        
        # prata med dorropnare och be dem tana
        try:
            if len(rows)>0:
                requests.get('http://192.168.42.10:5000/light/on', timeout=0.1)
            else:
                requests.get('http://192.168.42.10:5000/light/off', timeout=0.1)
        except (requests.exceptions.Timeout, requests.ConnectionError):
            pass


    time.sleep(3)
