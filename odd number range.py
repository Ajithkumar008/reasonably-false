N,Q=map(int,input("enter two values").split())
if(N<=10000 and Q<=10000):
    for i in range(N,Q,1):
        if(i%2==1):
            print (i,end=" ")
else:
    print("range  is only between 10000")
    
        
 

