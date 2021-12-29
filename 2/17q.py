n=int(input())
m=int(input())
x=int(input())
y=int(input())



if x<y:
    if n-x<x:
        print("n-x", n-x)
    elif m-x<x:
        print("m-x", m-x)
    else:
        print("x", x)
else:
        if n-y<y:
         print("n-y", n-y)
        elif m-y<y:
         print("m-y", m-y)  
        else: print("y", y)