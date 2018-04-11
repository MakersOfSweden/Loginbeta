#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Admin script to change user nick. """

import users

oldnick = input("Enter user old nick:")
newnick = input("Enter user new nick:")
    
users.update_nick(newnick, oldnick)
