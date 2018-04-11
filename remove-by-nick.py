#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Admin script to remove user by nick. """

import users

nick = input("Enter nick of the user to remove:")
    
users.remove(nick)
