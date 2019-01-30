N,K=map(int,input("enter values of N,K").split())
if N>K:
    x=list(map(int,input("enter N values").split()))
    if len(x)==N:
        summ=0
        for i in range(K):
            summ=summ+x[i]
        print(summ)
    else:
        print("do maintain range")
else:
    print("N should be greater than K")
