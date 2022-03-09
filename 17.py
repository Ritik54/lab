''' write a program to enter the cordinates of 2 points (x1,y1) and (x2,y2) and then 
find the distance between these 2 points'''

x1=float(input("enter the value of x1:"))
y1=float(input("enter the value of y1:"))

x2=float(input("enter the value of x2:"))
y2=float(input("enter the value of y2:"))

d=((x2-x1)**2+(y2-y1)**2)**0.5
print(d)