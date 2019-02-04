x,y=map(int,input("enter two numbers").split())
for i in range(x,y+1):
    summ=0
    pro=i
    while pro>0:
        summ=summ+(pro%10)**3
        pro=pro//10
    
    if(summ==i):
        print(summ)
