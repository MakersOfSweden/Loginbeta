#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Admin script to remove user with almost no time logged. """

import users

users.purge_inactive_users()
