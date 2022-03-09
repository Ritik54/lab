#currency

a=int(input("enter the amount with draw:"))
ahundred=1
a=a-100
twothousand =a//200
rem=a%2000
fivehundred=rem//500
r=rem%500
hundred=r//100

print("no of 2000 notes:",twothousand)
print("no of 500 notes:",fivehundred)
print("no of 100 notes",ahundred+hundred)