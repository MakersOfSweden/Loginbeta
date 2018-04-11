#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Admin script to move time from one user to another. """

import users

fromNick = input("Enter nick to move time from:")
toNick = input("Enter nick to add time to:")

users.move_time(fromNick, toNick)
