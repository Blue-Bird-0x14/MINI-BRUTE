import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    from GIGA import void
elif bit == '32bit':
    exit('32 NOT SAPPORTED')
