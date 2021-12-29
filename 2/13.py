x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if (x1==x2+1 or x1==x2-1) and y1==y2:
    print ("yes")
        
elif (y1==y2+1 or y1==y2-1) and x1==x2:
    print ("yes")
    
elif (x1==x2+1 and y1==y2+1) or (x1==x2-1 and y1==y2-1):
     print ("yes")
     
elif (x1==x2+1 and y1==y2-1) or (x1==x2-1 and y1==y2+1):
     print ("yes")     

else:
    print("no")