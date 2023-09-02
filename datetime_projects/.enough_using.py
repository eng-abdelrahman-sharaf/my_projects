# cautions
    # to open with start up this file should be in D:\my_files\my_projects\programming_concepts
    # and it name is enough_using.py
    # and loading_bar should be in its location below

from time import time , sleep
from os import system
start = time()/60
while True:
    now = time()/60
    duration = now - start

    # healthy duration control in mins
    healty = 60

    loading = duration/healty
    
    print(now)

    system(f"python.exe ..\\animation_projects\\loading_bar_cli.py {loading}")
    sleep(1)
    if loading >=1 :
        # it will hypernates pc 
        system("rundll32.exe powrprof.dll, SetSuspendState Sleep")
        start = start = time()/60