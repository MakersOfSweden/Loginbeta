#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Simple script for registering members coming and going. """

import sqlite3 as lite
import time
import requests
import hasher
import getpass
while True:
    while True:
        try:
            temp = getpass.getpass("Blip me! ")
            rfId = hasher.encode(temp)
            break
        except ValueError:
            print("Blip not recognised")
    print("")

    connection = lite.connect('People.db')
    connect.row_factory = lite.Row

    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM People WHERE blipId = ?", (rfId,))
        data = cur.fetchone()

        if data is None:  # there is no user with this ID tag
            print("-----------------------------------------------")
            print('There is no rfidtag named ', rfId, ' creating instance!')

            nick_temp = input("input your nick: ")

            cur.execute("INSERT INTO People VALUES (?,?,?,?,?);",
                        (rfId, nick_temp, 1, 0, time.time()))
            requests.put('http://127.0.0.1:5001/', json = {'who': nick_temp, 'what': "login"})
            try:
                requests.get('http://192.168.42.12:5000/',timeout=0.001)
            except:
                print(" ")
            print('you now exist and are logged in! dont forget to logout!')
            print("-----------------------------------------------")
        else:           # there is user with this ID tag
            if data['isHere']:  # is logged in => log hen out
                time_spent = time.time() - data['lastLogin']
                new_total_time = time_spent + data['totalTime']
                cur.execute("UPDATE People SET totalTime=?, isHere=? WHERE blipId=?",
                            (new_total_time, 0, rfId))
                requests.put('http://127.0.0.1:5001/', json = {'who': str(data['Nick']), 'what': "logout"})
                try:
                    requests.get('http://192.168.42.12:5000/',timeout=0.001)
                except:
                    print(" ")
                print("-----------------------------------------------")
                print("Goodbye " + str(data[2]) + " your highscore is: " +
                      str(new_total_time))
                print("-----------------------------------------------")

            else:   # is not logged in => log hen in
                cur.execute("UPDATE People SET lastLogin=?, isHere=? WHERE blipId=?",
                            (time.time(), 1, rfId))
                requests.put('http://127.0.0.1:5001/', json = {'who': str(data['Nick']), 'what': "login"})
                try:
                    requests.get('http://192.168.42.12:5000/',timeout=0.001)
                except:
                    print(" ")
                print("-----------------------------------------------")
                print("Welcome " + str(data['Nick']))
                print("-----------------------------------------------")
