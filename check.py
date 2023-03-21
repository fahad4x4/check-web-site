#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A script to check the status of websites
# Created by [FAHAD ALGHATHBAR]

import requests
from colorama import Fore, Style
from tabulate import tabulate

websites = [
    "https://GOOGLE.COM",
    "https://GOOGLE.COM",
    "https://GOOGLE.COM",
]

headers = ["Website", "Status", "HTTP Code"]
table = []

for website in websites:
    try:
        response = requests.get(website)
        response.raise_for_status()
        status = f"{Fore.GREEN}UP{Style.RESET_ALL}"
        code = response.status_code
    except requests.exceptions.RequestException as e:
        status = f"{Fore.RED}DOWN{Style.RESET_ALL}"
        code = str(e)

    table.append([website, status, code])

print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
