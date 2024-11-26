#!/usr/bin/python3

"""
---------------------------------------
Resolves Country, city and company of provided IP address.

GNU/Linux, BSD, OS X and Windows supported.
Author: iva
Date: 16.08.2024
---------------------------------------
"""

import os
import json
import urllib.request as urllib2


def get_ip_details(ip_address: str) -> str | None:
    try:
        url: str = "http://ip-api.com/json/"
        response = urllib2.urlopen(url + ip_address)
        data = response.read()
        values = json.loads(data)
        print(values)

    except subprocess.CalledProcessError as error:
        print(f"[!] Error: An error occurred: {error}")


def ip_resolver() -> None:
    ip_address: str = input("[==>] Enter IP address: ")
    get_ip_details(ip_address)


if __name__ == "__main__":
    ip_resolver()
