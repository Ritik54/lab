#WRITE A PROGRAM TO calculate compound interest 

principal=int(input("Enter the principal amount in rs : "))
rate=int(input("Enter the rate : "))
time=int(input("Enter the time : "))
ci=principal*((1+rate/100)**time)-principal
print("Compound Intrest is",ci)
