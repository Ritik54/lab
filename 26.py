# in a farm house there were some rabbits and chicken total head count of both is 72
#and leg count is=20 find the number of rabbit and chicken



head=int(input("enter the total number of head"))
leg=int(input("enter the total no legs"))
rabbit=(leg//2-head)
cock=2*head-(leg//2)

print("no of rabbit:",rabbit)
print("no of cock:",cock)