# Import Section
import os
import getpass
import platform
import readline

# Initiolize
# # Define Commands List
COMMANDS = ['cd', 'mkdir', 'python', 'python3']
COMMANDS_AW = COMMANDS
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
    # # pring Prompt
    print(color.WHITE + os.getcwd())
    print(INPUT)
    work = input('$ ')

    # # add chenge dir command
    if work.split(' ')[0] == 'cd':
        try:
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
        if work == 'ls':
            os.system('dir')
            continue

    # # Run Command
    os.system(work)