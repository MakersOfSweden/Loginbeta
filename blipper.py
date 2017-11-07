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
            rfid = hasher.encode(temp)
            break
        except ValueError:
            print("Blip not recognised")
    print("")

    return rfid


def add_user(nick, rfid):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO People VALUES (?,?,?,?,?);", (rfid, nick_temp, 1, 0, time.time()))
    return cursor.lastrowid


def log_action(who, what):
    requests.put('http://127.0.0.1:5001/', json = {'who': who, 'what': what})


def trigger_random_sound():
    try:
        requests.get('http://192.168.42.12:5000/',timeout=0.001)
    except:
        pass


def mark_as_logged_out(rfid):
    cursor = connection.cursor()
    cursor.execute('UPDATE People SET totalTime=totalTime + (strftime("%s", "now") - lastLogin), isHere=0 WHERE blipId=?', [rfid])


def mark_as_logged_in(rfid):
    cursor = connection.cursor()
    cursor.execute('UPDATE People SET lastLogin=strftime("%s", "now"), isHere=1 WHERE blipId=?', [rfid])


def fetch_user(rfid):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM People WHERE blipId = ?", [rfid])
    return cursor.fetchone()


while True:
    rfid_tag_id = wait_for_valid_rfid()

    connection = lite.connect('People.db')
    connect.row_factory = lite.Row

    with connection:
        user = fetch_user(rfid_tag_id)

        if not user:  # there is no user with this ID tag
            print("-----------------------------------------------")
            print('There is no rfidtag named {rfid}, creating user!'.format(rfid=rfid_tag_id))

            new_user_nick = input("input your nick: ")

            add_user(new_user_nick, rfid_tag_id)

            log_action(new_user_nick, 'login')

            trigger_random_sound()

            print('You now exist and are logged in! Dont forget to logout!')
            print("-----------------------------------------------")
        else:           # there is user with this ID tag
            if user['isHere']:  # is logged in => log hen out
                mark_as_logged_out(rfid_tag_id)

                log_action(user['Nick'], 'logout')

                trigger_random_sound()

                user = fetch_user(rfid_tag_id)

                print("-----------------------------------------------")
                print('Goodbye {Nick}, your highscore is: {totalTime}'.format(**user))
                print("-----------------------------------------------")

            else:   # is not logged in => log hen in
                mark_as_logged_in(rfid_tag_id)

                log_action(user['Nick'], 'login')

                trigger_random_sound()

                print("-----------------------------------------------")
                print("Welcome {Nick}!".format(**user))
                print("-----------------------------------------------")
