x=int(input("enter a number"))
if(x<=10000):   
    pro=x
    summ=0
    while(x>0):
        dig=x%10
        num=dig**3
        summ=summ+num
        x=x//10
    if(pro==summ):
        print("yes")
    else:
        print("No")
else:
    print("range is below 10000")
