#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Simple script for registering members coming and going. """

import sqlite3 as lite
import time
import requests
import util
import getpass
while True:
    while True:
        try:
            temp = getpass.getpass("Blip me! ")
            if temp:
                rfId = util.encode(temp)
                break
            else:
                print("Tagg id empty try again")
        except ValueError:
            print("Blip not recognised")
    print("")

    con = lite.connect('People.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM People WHERE blipId = ?", (rfId,))
        data = cur.fetchone()

        if data is None:  # there is no user with this ID tag
            print("-----------------------------------------------")
            print('There is no rfidtag named ', rfId, ' creating instance!')

            nick_temp = input("input your nick: ")
            if nick_temp:
                temp = cur.lastrowid
                if temp is None:
                    temp_id = 1
                else:
                    temp_id = temp + 1

                cur.execute("INSERT INTO People VALUES (?,?,?,?,?,?);",
                            (temp_id, rfId, nick_temp, 1, 0, time.time()))
                requests.put('http://127.0.0.1:5001/', json = {'who': nick_temp, 'what': "login"})
                try:
                    requests.get('http://192.168.42.12:5000/',timeout=0.001)
                except:
                    print(" ")
                print('you now exist and are logged in! dont forget to logout!')
                print("-----------------------------------------------")
            else:
                #Empty nick abort
                print("Nick empty blip again")
        else:           # there is user with this ID tag
            if data[3] is 1:  # is logged in => log hen out
                time_spent = time.time() - data[5]
                new_total_time = time_spent + data[4]
                cur.execute("UPDATE People SET totalTime=?, isHere=? WHERE blipId=?",
                            (new_total_time, 0, rfId))
                requests.put('http://127.0.0.1:5001/', json = {'who': str(data[2]), 'what': "logout"})
                try:
                    requests.get('http://192.168.42.12:5000/',timeout=0.001)
                except:
                    print(" ")
                print("-----------------------------------------------")
                print("Goodbye " + str(data[2]) + " your highscore is: " + util.toString(new_total_time))
                print("-----------------------------------------------")

            else:   # is not logged in => log hen in
                cur.execute("UPDATE People SET lastLogin=?, isHere=? WHERE blipId=?",
                            (time.time(), 1, rfId))
                requests.put('http://127.0.0.1:5001/', json = {'who': str(data[2]), 'what': "login"})
                try:
                    requests.get('http://192.168.42.12:5000/',timeout=0.001)
                except:
                    print(" ")
                print("-----------------------------------------------")
                print("Welcome " + str(data[2]))
                print("-----------------------------------------------")
