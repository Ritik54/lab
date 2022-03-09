#to calculate profit or loss where selling price and given price given by usercp=int(input("Enter the cost price :"))

cp=int(input("enter the cost value"))
sp=int(input("enter the selling price"))
if(sp>cp):
    print("he is in profit",(sp-cp))
else:
    print("he is in loss",(sp-cp))