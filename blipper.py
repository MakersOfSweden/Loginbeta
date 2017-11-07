#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Simple script for registering members coming and going. """

import sqlite3 as lite
import time
import requests
import hasher
import getpass

def wait_for_valid_rfid():
    while True:
        try:
            temp = getpass.getpass("Blip me! ")
            rfId = hasher.encode(temp)
            break
        except ValueError:
            print("Blip not recognised")
    print("")

    return rfId


def add_user(nick, rfid):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO People VALUES (?,?,?,?,?);", (rfId, nick_temp, 1, 0, time.time()))
    return cursor.lastrowid


def log_action(who, what):
    requests.put('http://127.0.0.1:5001/', json = {'who': who, 'what': what})


def trigger_random_sound():
    try:
        requests.get('http://192.168.42.12:5000/',timeout=0.001)
    except:
        pass




while True:
    rfid = wait_for_valid_rfid()

    connection = lite.connect('People.db')
    connect.row_factory = lite.Row

    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM People WHERE blipId = ?", (rfId,))
        data = cur.fetchone()

        if not data:  # there is no user with this ID tag
            print("-----------------------------------------------")
            print('There is no rfidtag named ', rfId, ' creating instance!')

            nick_temp = input("input your nick: ")

            add_user(nick_temp, rfId)

            log_action(nick_temp, 'login')

            trigger_random_sound()

            print('you now exist and are logged in! dont forget to logout!')
            print("-----------------------------------------------")
        else:           # there is user with this ID tag
            if data['isHere']:  # is logged in => log hen out
                time_spent = time.time() - data['lastLogin']
                new_total_time = time_spent + data['totalTime']
                cur.execute("UPDATE People SET totalTime=?, isHere=? WHERE blipId=?",
                            (new_total_time, 0, rfId))

                log_action(data['Nick'], 'logout')

                trigger_random_sound()

                print("-----------------------------------------------")
                print("Goodbye " + str(data[2]) + " your highscore is: " +
                      str(new_total_time))
                print("-----------------------------------------------")

            else:   # is not logged in => log hen in
                cur.execute("UPDATE People SET lastLogin=?, isHere=? WHERE blipId=?",
                            (time.time(), 1, rfId))

                log_action(data['Nick'], 'login')

                trigger_random_sound()

                print("-----------------------------------------------")
                print("Welcome " + str(data['Nick']))
                print("-----------------------------------------------")
