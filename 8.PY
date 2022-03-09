#WRITE A PROGRAM TO FIND OUT AREA OF RECTANGLE
a1=int(input("Enter the  side 1 : "))
a3=int(input("Enter the  side 3 : "))
a2=int(input("Enter the  side 2 : "))
#first we find semi parimeter
s=(a1+a2+a3)/2
area=(s*(s-a1)*(s-a2)*(s-a3))**0.5
print("Area of the scalen triangle is %d unit^2"%area)