from colored import fg, attr, bg
import subprocess
import psutil

commands = [
    'help',
    'balance',
    'config',
    'exit',
    'miners'
]

def func_exit():
   print(f'{fg(46)}Exiting...{fg(15)}')
   exit()

def func_help():
   print(f"""{fg(46)}Commands List\n{fg(155)}> help{attr(0)} - (Shows this message){fg(155)}\n> mine{attr(0)} - (Enter mining section){fg(155)}\n> config{attr(0)} - (Edits config.json){fg(155)}\n> exit{attr(0)} - (Exits the app){fg(155)}
   """)

def func_unknowncmd():
   print(f'{fg(1)}Command not found! Please type "help" for commands list!')

def func_nochoice():
   print(f'{fg(155)}BetterSalad:{fg(105)}~{fg(155)}${fg(15)} ', end='')

def func_miners():
   print(f'{fg(46)}Availiable Miners\n{fg(220)}[GPU] T-Rex {attr(0)}- ({fg(120)}NVIDIA{attr(0)})\n{fg(220)}[GPU] Phoenix {attr(0)}- ({fg(120)}NVIDIA{attr(0)}/{fg(160)}AMD{attr(0)})\n{fg(220)}[GPU] NBMiner {attr(0)}- ({fg(120)}NVIDIA{attr(0)}/{fg(160)}AMD{attr(0)})\n{fg(220)}[GPU] TeamRed {attr(0)}- ({fg(160)}AMD{attr(0)})\n{fg(220)}[GPU] lolMiner {attr(0)}- ({fg(120)}NVIDIA{attr(0)}/{fg(160)}AMD{attr(0)})\n{fg(220)}[CPU] XMRig {attr(0)}- ({fg(25)}INTEL{attr(0)}/{fg(202)}RYZEN{attr(0)})')


def func_selectminer():
   print(f'{fg(46)}Availiable Miners\n{fg(220)}XMRig{attr(0)}')

cpucores = psutil.cpu_count(logical=False)
cpuname = subprocess.check_output('wmic path win32_Processor get name').decode().split('Name')[1].strip('\n\r ')

gpu = subprocess.check_output('wmic path win32_VideoController get name').decode().split('Name')[1]
gpu = gpu.strip('\r').strip('\n').strip('').splitlines()[2]

print(f"""{fg(155)}
                       ..                         
                   ......                         
                  .......                         
                      ...         ....            
                         .        .......         
                         --:.     ....            
                         ------:  .               
              .::        ------::                  {fg(46)} ____       _   _            _____       _           _ {fg(155)}
           .:---:        ---:....                  {fg(46)}|  _ \     | | | |          / ____|     | |         | |{fg(155)}
         -------:       :........        .         {fg(46)}| |_) | ___| |_| |_ ___ _ _| (___   __ _| | __ _  __| |{fg(155)}
           .:---:   .-+##    ....     .---         {fg(46)}|  _ < / _ \ __| __/ _ \ '__\___ \ / _` | |/ _` |/ _` |{fg(155)}
              .:::=*#####       ...:------         {fg(46)}| |_) |  __/ |_| ||  __/ |  ____) | (_| | | (_| | (_| |{fg(155)}
             .-+*+*######      .-+*+=-----         {fg(46)}|____/ \___|\__|\__\___|_| |_____/ \__,_|_|\__,_|\__,_|{fg(155)}
          :=*###*+++++*##  .:----+####*+=-               {fg(15)}Presented and Powered by: {fg(155)}NoError Studios™️
        .+######*+++++++*--------+######+:         
           :+###*++++*###++===---+###+:            {fg(15)}GPU: {fg(105)}{gpu}{fg(155)}
              .=+**######+++++=====.               {fg(15)}CPU: {fg(105)}{cpuname} ({cpucores}){fg(155)}
                  :+#####++++=-:                  
                     .=*#+=:.                      
""")
text = f'{fg(155)}BetterSalad:{fg(105)}~{fg(155)}${fg(15)} '
while True:
   print(text, end='')
   choice = str(input())
   if choice == '':
      func_nochoice()
   elif choice == 'help':
      func_help()
   elif choice == 'exit':
      func_exit()
   elif choice == 'miners' or choice == 'miner':
      func_miners()
   elif choice == 'mine':
      text = f'{fg(155)}BetterSalad/mine:{fg(105)}~{fg(155)}${fg(15)} '
      print(f'{fg(155)}Select type of miner {fg(240)}(CPU/GPU): {attr(0)}', end='')
      minetypechoice = str(input())
      if minetypechoice == 'cpu' or minetypechoice == 'CPU':
         func_selectminer()
   else:
      func_unknowncmd()