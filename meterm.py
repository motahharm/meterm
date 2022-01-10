# Import Section
import os
import getpass
import platform
import readline
import json
from types import coroutine

# Initiolize
# # Define Commands List
COMMANDS = ['cd', 'mkdir', 'python', 'python3']
COMMANDS_AW = COMMANDS

# add config.json
config = ''
if os.path.isfile('config.json'):
    with open('config.json', 'r') as conf:
        config = json.load(conf)
else :
    with open('config.json', 'a') as conf:
        data = '{'

        data += '"dirs":{'
        data += '"home":{cwd}'.format(cwd=('"' + os.getcwd().replace('\\'[0], '/') + '"'))
        data += '}'

        data += '}'
        conf.write(data)
    with open('config.json', 'r') as conf:
        config = json.load(conf)
config_dir = {}
config_dir = config['dirs']


# # Create Auto Complate Function
def complete(text, state):
    for cmd in COMMANDS_AW:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1
# # Define Colors For Terminal
class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
# # Define Input Prompt Text
INPUT = color.GREEN + getpass.getuser()
INPUT += color.RED + '@'
INPUT += color.GREEN + platform.node()
INPUT += color.WHITE
# # Initilize For First Run
onlyfiles = [f for f in os.listdir(os.getcwd())]
COMMANDS_AW = COMMANDS + onlyfiles
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
# # If Venv Is Activate
if os.getenv('VIRTUAL_ENV'):
    addr = os.environ['VIRTUAL_ENV'].split("\\"[0])
    INPUT = color.RED +'('+ addr[len(addr)-1] +') '+ INPUT

# Ultimate While For Run Commands
while True:
    try:
        # # pring Prompt
        print(color.WHITE + os.getcwd())
        print(INPUT)
        work = input('$ ')

        # # Exit Form Meterm
        if work.split(' ')[0] == 'exit':
            break
        if work.startswith('mt-ad ') or work.startswith('mt-add_dir '):
            print(config)
            os.remove('config.json')
            with open('config.json', 'a') as conf:
                config_dir[work.split(' ')[1]] = work.split(' ')[2]
                config['dirs'] = config_dir
                json.dump(config, conf)
            coroutine
        # # add chenge dir command
        if work.split(' ')[0] == 'cd':
            try:
                if work.split(' ')[1] in config_dir:
                    os.chdir(config_dir[work.split(' ')[1]])
                    onlyfiles = [f for f in os.listdir(os.getcwd())]
                    COMMANDS_AW = COMMANDS + onlyfiles
                    readline.parse_and_bind("tab: complete")
                    readline.set_completer(complete)
                    continue
                if os.path.isdir(work.split(' ')[1]):
                    os.chdir(work.split(' ')[1])
                else:
                    os.chdir(os.getcwd() + '\\'[0] +work.split(' ')[1])
            except:
                print('That Is Not Real Dir')
            onlyfiles = [f for f in os.listdir(os.getcwd())]
            COMMANDS_AW = COMMANDS + onlyfiles
            readline.parse_and_bind("tab: complete")
            readline.set_completer(complete)
            continue

        # # add Some Command On Windows
        if os.name == 'nt':
            if work == 'clear':
                os.system('cls')
                continue
            if work == 'pwd':
                print(os.getcwd())
                continue
            if work == 'ls':
                os.system('dir')
                continue
            if work.startswith('touch '):
                with open(work.split(' ')[1], 'a') as file:
                    file.write('')
                continue

        # # Run Command
        os.system(work)
    except:
        print('An Eror In This Command')