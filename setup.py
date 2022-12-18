import os
import requests
import urllib.request
import shutil

def find_nh_rig():
    appdata = os.getenv('APPDATA')
    try:
        log = open(f'{appdata}\Salad\logs\main.old.log', 'r', encoding='UTF-8')
        readlogs = log.read()
        seperateNH = readlogs.split('NiceHash rig ID: ')[1]
        NHRIG = seperateNH[0:15]
    except:
        log = open(f'{appdata}\Salad\logs\main.log', 'r', encoding='UTF-8')
        readlogs = log.read()
        seperateNH = readlogs.split('NiceHash rig ID: ')[1]
        NHRIG = seperateNH[0:15]
    return NHRIG

def find_em_rig():
    appdata = os.getenv('APPDATA')
    try:
        log = open(f'{appdata}\Salad\logs\main.old.log', 'r', encoding='UTF-8')
        readlogs = log.read()
        seperateEM = readlogs.split('Ethermine worker ID: ')[1]
        EMRIG = seperateEM[0:15]
    except:
        log = open(f'{appdata}\Salad\logs\main.log', 'r', encoding='UTF-8')
        readlogs = log.read()
        seperateEM = readlogs.split('Ethermine worker ID: ')[1]
        EMRIG = seperateEM[0:15]
    return EMRIG

def find_nh_wallet():
    appdata = os.getenv('APPDATA')
    try:
        log = open(f'{appdata}\Salad\logs\main.old.log', 'r', encoding='UTF-8')
        readlogs = log.read()
        seperateNHWT = readlogs.split('NiceHash wallet address: ')[1]
        NHWALLET = seperateNHWT[0:34]
    except:
        log = open(f'{appdata}\Salad\logs\main.log', 'r', encoding='UTF-8')
        readlogs = log.read()
        seperateNHWT = readlogs.split('NiceHash wallet address: ')[1]
        NHWALLET = seperateNHWT[0:34]
    return NHWALLET

def find_em_wallet():
    appdata = os.getenv('APPDATA')
    try:
        log = open(f'{appdata}\Salad\logs\main.old.log', 'r', encoding='UTF-8')
        readlogs = log.read()
        seperateEMWT = readlogs.split('Ethermine wallet address: ')[1]
        EMWALLET = seperateEMWT[0:42]
    except:
        log = open(f'{appdata}\Salad\logs\main.log', 'r', encoding='UTF-8')
        readlogs = log.read()
        seperateEMWT = readlogs.split('Ethermine wallet address: ')[1]
        EMWALLET = seperateEMWT[0:42]
    return EMWALLET

def make_miners_folder():
    if not os.path.exists('miners'):
        os.mkdir('miners')
make_miners_folder()