import requests
import urllib
import shutil
import os
from colored import fg, attr
import json

api = requests.get('https://raw.githubusercontent.com/RadsammyT/SaladBind-Archive/8bb7fde1c96e185fb1b5f4e61dfd3cb334f6197f/internal/miners.json').json()

def download_miner(miner):
    try:
        print(f'{fg(155)}Select miner to remove\n{fg(220)}[1] T-Rex {attr(0)}\n{fg(220)}[2] Phoenix {attr(0)}\n{fg(220)}[3] NBMiner {attr(0)}\n{fg(220)}[4] TeamRed {attr(0)}\n{fg(220)}[5] lolMiner {attr(0)}\n{fg(220)}[6] XMRig {attr(0)}', end='')
        mchoice = int(input())
        if mchoice == 1:
            minerjson = 't-rex'
        elif mchoice == 2:
            minerjson = 'phoenixminer'
        elif mchoice == 3:
            minerjson = 'nbminer'
        elif mchoice == 4:
            minerjson = 'teamredminer'
        elif mchoice == 5:
            minerjson = 'lolminer'
        elif mchoice == 6:
            minerjson = 'xmrig'
        link = api['miners'][minerjson]['download']['win32']
        urllib.request.urlretrieve(link, os.getcwd()+f'/miners/{miner}.zip')
        shutil.unpack_archive(filename=os.getcwd()+f'/miners/{miner}.zip', extract_dir=os.getcwd()+f'/miners/{miner}')
        os.remove(path=os.getcwd()+f'/miners/{miner}.zip')
        f = open(os.getcwd()+'/miners/miners.json', 'w')
        j = json.load(f)
        j['']
    except:
        print(f'There was an error installing {miner} miner! Please try again.')

def remove_miner(miner):
    print(f'{fg(155)}Select miner to remove\n{fg(220)}[1] T-Rex {attr(0)}\n{fg(220)}[2] Phoenix {attr(0)}\n{fg(220)}[3] NBMiner {attr(0)}\n{fg(220)}[4] TeamRed {attr(0)}\n{fg(220)}[5] lolMiner {attr(0)}\n{fg(220)}[6] XMRig {attr(0)}', end='')
    mchoice = int(input())
    if mchoice == 1:
        toremove = api['miners']['trex']['parameters']['filename']+'-'+api['miners']['trex']['version']+'-win'
    elif mchoice == 2:
        toremove = api['miners']['phoenixminer']['parameters']['filename']+'_'+api['miners']['phoenixminer']['version']+'_Windows'
    elif mchoice == 3:
        toremove = +'NBMiner-'+api['miners']['nbminer']['version']+'_Win'
    elif mchoice == 4:
        toremove = api['miners']['teamredminer']['parameters']['filename']+'-v'+api['miners']['trex']['version']+'-win'
    elif mchoice == 5:
        minerjson = 'lolminer'
    elif mchoice == 6:
        minerjson = 'xmrig'
    try:
        if os.path.exists(os.getcwd()+f'/miners/{toremove}'):
            os.remove(path=os.getcwd()+f'/miners/{toremove}')
        else:
            print(f'{fg(1)}{miner} was not found in /miners/ folder! Skipping...')
    except:
        print(f'{fg(1)}There was an error removing {miner} miner! Please try again.')

remove_miner(miner='Phoenix')