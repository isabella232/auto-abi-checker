#!/usr/bin/env python3

# Copyright 2018 Open Robotics
# Licensed under the Apache License, Version 2.0

from subprocess import check_call
from sys import stderr


def _check_call(cmd):
    print(" - Run '%s'" % ' '.join(cmd))

    try:
        check_call(cmd)
    except Exception as e:
        print(str(e))
        return e

    return 0


def error(msg):
    print("\n [err] " + msg + "\n", file=stderr)
    exit(-1)


def warn(msg):
    print("\n [warn] " + msg + "\n", file=stderr)


def comma_list_to_array(str_input):
    if "," in str_input:
        return str_input.split(",")

    return [str_input]
