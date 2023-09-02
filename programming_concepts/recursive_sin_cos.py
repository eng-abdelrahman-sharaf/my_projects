# making sin and cos using recursion 

pi = 3.14159265358979323846

def sin(n):
    if n < 10 :
        return n * pi / 180
    else :
        result = sin(n/2)*cos(n/2)*2
        return result
    
def cos(n):
    if  80 < n and n <= 90:
        return   pi/2 - n * pi / 180
    else:
        return 1 - 2 * sin(n/2)**2


for l in [30 , 0 , 90 ]:
    print(f"sin({l}) = %.2f"%sin(l))

for l in [60 , 90 , 0 ]:
        print(f"cos({l}) = %.2f"%cos(l))