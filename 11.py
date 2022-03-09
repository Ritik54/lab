# #WRITE A PROGRAM TO swap to numberss
# # conditions   >>>
# #1> with out using third variable
# #2> using bitwise operator
# #3> using third variable

# from calendar import c


a=5
b=10
print("value of a is {0} and b is {1} before swap".format (a,b))
a=a+b
b=a-b
a=a-b
print("value of a is{0} and b is {1} after swap".format (a,b))



#bitwise operator
a=10
b=5
print("the value of a is{0} and b is {1} before swap".format(a,b))
a=a^b
b=a^b
a=a^b
print("the value of a is {0} and b is {1} after swapping".format(a,b))


# using third variable

a=10
b=5
print("the value of a is{0} and b is {1} before swap".format(a,b))
c=a
a=b
b=c
print("the value of a is {0} and b is {1} after swap".format(a,b))