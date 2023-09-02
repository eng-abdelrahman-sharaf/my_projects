"""
in this file you have 3 controllers
- sleep for the speed of rotation
- z_pace also for the speed of rotation
- x_pace for precision
"""

from math import ceil , sqrt
from time import sleep

# circle file
file = open("circle.data" , "w+")

def plot(x , y):
    file.write(f"\033[{y};{x}f-")

r = 10


# erase the cursor
print("\033[?25l")


# set the origin
o_x = ceil(20 * 16/9)
o_y = 20

# x pace controls the shape of the circle
x_pace = 0.05
sign = 1 # the sign of x pace 

# z pace controls the rotation degree 
z_pace = 0.5

# initial value
z = 0


# for closing the file we use this try except statement
try:

    while True:
        # erase the screen
        print("\033[2J")

        # file clearing
        file = open("circle.data" , "w+")

        # saving z value
        save = z

        x = -r * sign 
        while x<=r and x>=-r:
            y  = (r**2 - x**2)**0.5
            if abs(z) > abs(x) : z = x 
            if x >=0 : x_ = sqrt(x**2-z**2)
            else : x_ = -sqrt(x**2 - z**2)


            # plotting values
            x_p = o_x + ceil(16/9 * x_) #every x has 2 y
            y_p = o_y + ceil(y) # +y 
            plot(x_p , y_p)
            y_p = o_y - ceil(y) # +y 
            plot(x_p , y_p)

            # current x
            x_1 = x

            # upcoming x
            x_2  = x = x + x_pace


            # to avoid zero division error
            if x_2 == 0:
                # plot it then increment x
                plot(o_x ,o_y + r)
                plot(o_x ,o_y - r)
                # upcoming x
                x_2  = x = x + x_pace


            # upcoming z
            z = z* x_2/x_1

        # setting the cursor at top
        file.seek(0)
        
        # coloring
        print("\033[33m")

        # printing the circle
        print(file.read() , flush=True)

        z = save

        if z in [r , -r]:
            # z_pace *= - the_sign_of_r
            z_pace = abs(z_pace) * -1 *sqrt(z**2)/z
            sign *= -1
            x_pace*=-1


        # it also controls the speed of rotation
        sleep(0.02)



        z+= z_pace

except KeyboardInterrupt:
    print("\033[2J" , "\033[H" , "thanks for watching :)".center(40) , sep='')

# closing the file whatever happened 
except :
    pass

finally:
    file.close()