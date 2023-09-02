# initialize the counter
num = 1
direction = 1

while True:

    # enter the length of the horizontal 
    # controls the size of the diamond
    horizontal_length = int(input("enter the length of the horizontal line (must be odd) : "))

    # for error handling
    errors = ""
    if horizontal_length % 2 == 0:
        errors += "please check that the number is odd and "
    if horizontal_length > 101 :
        errors += "the number is too big and "
    if horizontal_length <= 0 :
        errors += "please enter a valid number and "
    if errors == "":
        break
    print(errors[:-5])
    


# color as usual :)
print("\033[34m" , end='')

while True:

    # print the shape
    print(" "*int((horizontal_length - num)/2) , "*"*num , sep='')
    
    # makes the reversed shape 
    if num == horizontal_length :
        direction*=-1
    
    # breaking the loop condition
    if num == 1 and direction == -1:
        break
    
    # increment or decrement depending on direction
    num+= direction * 2