employees = [('C',85),('A',90),('B',70)]
print(employees)
sorted_employees=sorted(employees,key=lambda x:x[0],reverse=True) #--if reverse is false then it will be in order
print(sorted_employees)
