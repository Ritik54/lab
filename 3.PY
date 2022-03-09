#CHECK WEATHER LAST DIGIT BINARY NUMBER 1 OR 0..?
a=int(input("Enter the number: "))
n=a%10
b=n&1
print("Last binary digit is ",b)