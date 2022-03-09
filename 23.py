#you have generate a sallaery of employe conditions are..>
#1..> if basic sallary is<10000than hra will be 80% of basic sallay 
# and da will be 90%of basic sallary..?

#2..> if basic sallary is greater than 10000 and less than equal to 20000 than hra will be
#85% of basic sallary and da will be 95%..?

#3..>if basic sallary is greater than 20000 than hra will be 95% and da will be 95% 
#than calculate the sallary of empolye
s=int(input("enter your basic sallary: "))
if(s<=1000):
    hra=(s*80)//100
    da=(s*90)//100
    print("your total sallary is",hra+da+s)

if(s>1000 and s<20000):
    hra=(s*85)//100
    da=(s*95)//100
    print("your total sallary is",hra+da+s)
if(s>2000):
    hra=(s*95)//100
    da=(s*95)//100
    print("total sallary is",hra+da+s)