#!/usr/bin/env python3

from datetime import datetime
import subprocess
from os import path
import config

DATE_FILE = "last-updated.conf"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

try:
    with open(DATE_FILE, "r") as f:
        last_date = datetime.strptime(f.readline().rstrip("\n"), DATE_FORMAT)
except IOError:
    last_date = datetime.fromtimestamp(0)

current_date = datetime.now()
if current_date.date() > last_date.date():
    result = subprocess.run(["./wallpaper.sh", config.URL], cwd = path.abspath(path.dirname(__file__)))
    if not result.returncode:
        with open(DATE_FILE, "w") as f:
            f.write(current_date.strftime(DATE_FORMAT))
