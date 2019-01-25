yr=int(input())
if yr%4==0:
   if yr%100==0:
       if yr%400==0:
           print(" leap year")
       else: 
              print(" not a leap year")
   else:
        print(" leap year")
else:
     print(" not a leap year")
