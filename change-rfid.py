#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Admin script to change user rfid. """

import users
import util
import getpass

oldid = util.encode(getpass.getpass("Enter user old rfid:"))
newid = util.encode(getpass.getpass("Enter user new rfid:"))

users.update_rfid(newid, oldid)
