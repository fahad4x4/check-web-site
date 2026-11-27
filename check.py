#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A script to check the status of websites
# Created by [FAHAD ALGHATHBAR]

import requests
from colorama import Fore, Style
from tabulate import tabulate

# Edit this list with the websites you want to check
websites = [
    "https://www.google.com",
    "https://github.com",
    "https://www.wikipedia.org",
]

TIMEOUT = 10  # seconds per website

headers = ["Website", "Status", "HTTP Code"]
table = []

for website in websites:
    try:
        response = requests.get(website, timeout=TIMEOUT, headers={"User-Agent": "check-web-site/1.0 (+https://github.com/fahad4x4/check-web-site)"})
        response.raise_for_status()
        status = f"{Fore.GREEN}UP{Style.RESET_ALL}"
        code = response.status_code
    except requests.exceptions.RequestException as e:
        status = f"{Fore.RED}DOWN{Style.RESET_ALL}"
        code = str(e)

    table.append([website, status, code])

print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
