#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('X-Request-Id'))
