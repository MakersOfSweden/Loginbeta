#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Dev script to change user rfid of a user specified by nick. """

import users
import util

nick = input("Enter user nick:")
newRfid = util.encode(getpass.getpass("Enter user new rfid:"))

users.change_rfid(newRfid, nick)
