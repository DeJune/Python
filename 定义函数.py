import math
def quadratic(a,b,c):
    d = b*b-4*a*c
    if d < 0:
        print('无解')
    elif d == 0:
        x = (-b/(2*a))
        return x
    else :
        x1=(math.sqrt(b*b-4*a*c)+b)/(2*a)
        x2=(math.sqrt(b*b-4*a*c)-b)/(2*a)
        return x1,x2
