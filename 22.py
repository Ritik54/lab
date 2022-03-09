#calculate the number of apple if...
#a man have some apple if he make pair of 7,7 then no of free apple , if
# he make pair of 6,5,4,3,2 than an apple free
num=int(input("enter the number:"))
if(num%7==0 and num%6==1 and num%5==1 and num%4==1 and num%3==1 and num%2==1):
    print(num,"number is correct")
else:
    print("input is invalid")


