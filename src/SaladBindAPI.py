import requests
import urllib
import shutil
import os
from colored import fg, attr
import json

api = requests.get('https://raw.githubusercontent.com/RadsammyT/SaladBind-Archive/8bb7fde1c96e185fb1b5f4e61dfd3cb334f6197f/internal/miners.json').json()

def download_miner():
    try:
        print(f'{fg(155)}Select miner to install\n{fg(105)}1) {fg(220)}[GPU] T-Rex {attr(0)}- ({fg(120)}NVIDIA{attr(0)})\n{fg(105)}2) {fg(220)}[GPU] PhoenixMiner {attr(0)}- ({fg(120)}NVIDIA{attr(0)}/{fg(160)}AMD{attr(0)})\n{fg(105)}3) {fg(220)}[GPU] NBMiner {attr(0)}- ({fg(120)}NVIDIA{attr(0)}/{fg(160)}AMD{attr(0)})\n{fg(105)}4) {fg(220)}[GPU] TeamRedMiner {attr(0)}- ({fg(160)}AMD{attr(0)})\n{fg(105)}5) {fg(220)}[GPU] lolMiner {attr(0)}- ({fg(120)}NVIDIA{attr(0)}/{fg(160)}AMD{attr(0)})\n{fg(105)}6){fg(220)} [CPU] XMRig {attr(0)}- ({fg(25)}INTEL{attr(0)}/{fg(202)}RYZEN{attr(0)})\n\n{fg(155)}BetterSalad/mine:{fg(105)}~{fg(155)}${fg(15)} ', end='')
        mchoice = int(input())
        if mchoice == 1:
            minerjson = 'trex'
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
        if not os.path.exists(os.getcwd()+f'/miners/{minerjson}'):
            link = api['miners'][minerjson]['download']['win32']
            print(f'{fg(155)}Downloading {minerjson}...')
            urllib.request.urlretrieve(link, os.getcwd()+f'/miners/{minerjson}.zip')
            print(f'{fg(155)}Unpacking miner...')
            shutil.unpack_archive(filename=os.getcwd()+f'/miners/{minerjson}.zip', extract_dir=os.getcwd()+f'/miners/{minerjson}')
            os.remove(path=os.getcwd()+f'/miners/{minerjson}.zip')
            print(f'{fg(155)}Cleaning up...')
            with open(os.getcwd()+'/miners/miners.json', 'r+') as f:
                data = json.loads(f.read())
                data[minerjson]['installed'] = 1
                data[minerjson]['version'] = api['miners'][minerjson]['version']
                f.seek(0)  
                json.dump(data, f)
                f.truncate()
        else:
            print(f'{fg(155)}{minerjson} already exists in /miners/ path!')
    except:
        print(f'{fg(1)}There was an error installing {minerjson} miner! Please try again.')

def remove_miner():
    print(f'{fg(155)}Select miner to remove\n{fg(105)}1) {fg(220)}[GPU] T-Rex {attr(0)}- ({fg(120)}NVIDIA{attr(0)})\n{fg(105)}2) {fg(220)}[GPU] PhoenixMiner {attr(0)}- ({fg(120)}NVIDIA{attr(0)}/{fg(160)}AMD{attr(0)})\n{fg(105)}3) {fg(220)}[GPU] NBMiner {attr(0)}- ({fg(120)}NVIDIA{attr(0)}/{fg(160)}AMD{attr(0)})\n{fg(105)}4) {fg(220)}[GPU] TeamRedMiner {attr(0)}- ({fg(160)}AMD{attr(0)})\n{fg(105)}5) {fg(220)}[GPU] lolMiner {attr(0)}- ({fg(120)}NVIDIA{attr(0)}/{fg(160)}AMD{attr(0)})\n{fg(105)}6){fg(220)} [CPU] XMRig {attr(0)}- ({fg(25)}INTEL{attr(0)}/{fg(202)}RYZEN{attr(0)})\n\n{fg(155)}BetterSalad/mine:{fg(105)}~{fg(155)}${fg(15)} ', end='')
    mchoice = int(input())
    if mchoice == 1:
        minerjson = 'trex'
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
    try:
        if os.path.exists(os.getcwd()+f'/miners/{minerjson}'):
            folder = os.getcwd()+'/miners/'+minerjson
            os.remove(folder)
        else:
            print(f'{fg(1)}{minerjson} was not found in /miners/ folder! Skipping...')
    except:
        print(f'{fg(1)}There was an error removing {minerjson} miner! Please try again.')