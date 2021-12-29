x = int(input())
y = int(input())
q = int(input())
w = int(input())

if x>8 or y>8 or q>8 or w>8 or x<1 or y<1 or q<1 or w<1:
    print ("Нет такой клетки")
    
elif x%2==0 and y%2==0 and q%2==0 and w%2==0:
    print ("yes")
    
elif x%2==1 and y%2==1 and q%2==1 and w%2==1:
    print ("yes")

elif x%2==1 and y%2==1 and q%2==0 and w%2==0:
    print ("yes")
    
elif x%2==0 and y%2==0 and q%2==1 and w%2==1:
    print ("yes")    
    
elif x%2==1 and y%2==0 and q%2==1 and w%2==0:
    print ("yes") 
    
elif x%2==0 and y%2==1 and q%2==0 and w%2==1:
    print ("yes")    
    
elif x%2==0 and y%2==1 and q%2==1 and w%2==0:
    print ("yes")  
    
elif x%2==1 and y%2==0 and q%2==0 and w%2==1:
    print ("yes")     
    
else:
    print ("no")