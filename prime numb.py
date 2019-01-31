#primenumber......ajith
x=int(input("enter a value"))
if x<=1000:
    if(x>1):
        for i in range(2,x):
            if(x%i==0):
                print("it is not a prime number")
                break
        else:
            print("it is a prime number")
    else:
        print("not a prime number")
else:
    print(" value should be less than 1000")
