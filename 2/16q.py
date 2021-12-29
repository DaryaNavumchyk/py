m=int (input())
n=int (input())
k=int (input())

s=m*n
a=s-n
b=s-m


if k<s:
    if k==1:
        print("no")
    elif k%m==0 or k%n==0:
        print ("yes")
    elif a%k==0 or b%k==0:
        print("yes")
    else:
        print("no")
else:
    print("no")
