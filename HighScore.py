#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import requests
import os
import time


def turn_lights_on():
    try:
        requests.get('http://192.168.42.10:5000/light/on', timeout=0.1)
    except (requests.exceptions.Timeout, requests.ConnectionError):
            pass

def turn_lights_off():
    try:
        requests.get('http://192.168.42.10:5000/light/off', timeout=0.1)
    except (requests.exceptions.Timeout, requests.ConnectionError):
            pass


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
            turn_lights_on()
        else:
            turn_lights_off()


    time.sleep(3)
