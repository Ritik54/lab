# FIND THE SUM OF LAST THREE DIGIT OF YOUR UNIVERSITY ROLL NUMBER 


n= int(input("enter the university rool number:"))
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
n=n//10

print("sum of last three digit nimber is",a+b+c)
