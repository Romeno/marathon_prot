# -*- coding: utf-8

import datetime


def calculate_age(born):
    now = datetime.datetime.now()
    return now.year - born.year - ((now.month, now.day) < (now.month, now.day))

