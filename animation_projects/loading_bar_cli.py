# a simple application on carriage return 
# and adding some colors from ansi escape sequences
from math import floor
from time import sleep
from sys import argv
def loading_bar(percentage ,time = 0.05):
        # max percentage is 100%
        if percentage>1:
            percentage = 1      
        
        # number of hashtags
        hash_num = int(percentage*10)
        
        print(f"\rloading \033[94m{percentage*100:.2f}\033[39m % [\033[94m{'#'*hash_num}\033[39m{' ' *(10-hash_num)}]" , end='')
        sleep(time)

if len(argv)==1:
    for i  in range(1 , 101):
        percentage = i/100
        loading_bar(percentage)
        
else :
    # to get percentage from command
    percentage = float(argv[1])
    
    loading_bar(percentage, 0)

# for ansi escape sequences reference
    # https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797