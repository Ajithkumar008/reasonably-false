n,k=map(int,input("Enter 2 numbers:").split())
for add in range(n+1,k):
    if(add>1):
        for i in range(2,add):
            if(add%i==0):
                break
        else:
            print(add)
