#input all sides of a triangle and check letter triangle is valid or not

a=int(input("enter the number of 1 side "))
b=int(input("enter the number of  2 side "))
c=int(input("enter the number of 3 side "))
if(a+b>c or b+c>a or a+c>b):
    print("triangle is valid")
else:
    print("Triangle is not valid ")
