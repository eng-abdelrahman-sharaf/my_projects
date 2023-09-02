from time import sleep

from math import ceil, floor
# !!! use print_ to avoid default \n
def print_(*args , **kargs):
    print(*args , end = '' , **kargs)

# origin

r = 10

print_("\033[?25l")

z = 0
while z <= r-0.001:

    print_(f"\033[2J\033[20;{ceil(20*16/9)}f.")
    # circle drawing
    x = -r
    while x<=r :
        # for rotation
        y = ceil((r**2 -x**2)**0.5)
        x_1 = x
        if x>=0 :x_ = (x**2 - z**2)**0.5 
        else :x_ = -(x**2 - z**2)**0.5 
        print_(f"\033[{y+20};{ceil(20*16/9) + ceil(x_*16/9)}f.")
        print_(f"\033[{-y+20};{ceil(20*16/9) + ceil(x_*16/9)}f.")

        # controls the precision
        x_2 = x = x +0.1

        z = abs(x_2 * z /x_1)


    #controls degree of rotation 
    z += .01
    sleep(0.1)

print_("\033[2J")
    
    


