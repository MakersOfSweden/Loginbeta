#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import lights
import users
import util


while True:
    os.system('clear')

    print("------------ Highscore ------------")

    highscore = users.highscore()

    for i, user in enumerate(highscore):
        print('{position}: {nick:10} score: {score}'.format(position=i+1, nick=user['Nick'], score=util.formatTime(user['totalTime'])))
    time.sleep(0.1)

    print("---------- People online ----------")

    logged_in_users = users.logged_in()
    
    for user in logged_in_users:
        print(user['Nick'])
    
    if logged_in_users:
        lights.on()
    else:
        lights.off()


    time.sleep(3)
