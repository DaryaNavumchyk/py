a=int(input())
b=int(input())
c=int(input())

if a<b and a<c:
    print (a)
elif b<c and b<c:
    print (b)
elif c<a and c<b:
    print (c)
elif a<b and a>c and c<b:
    print (a)
elif b<c and b>a and a<c:
    print (b)
elif c<a and c>b and b<a:
    print (c)
elif a==b and a<c:
    print (a)
elif a==c and a<b:
    print (a)
elif b==c and b<a:
    print (b)
else:
    print ("Они равны", a)
    
    