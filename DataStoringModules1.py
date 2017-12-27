#Basic Data storing modules

#dictionaries


#declare and init dict
employee={'name' : 'miri' ,'age':35 ,'fields of work':['yell','complain']}

#print certain key
print(employee['name'])

#validate if  exists correct way
print(employee.get('not exist'))

#add key
employee['favorite food']='All of it'

print(employee)

#update fields
employee.update({'name': 'miri','age':36})

print(employee)

#del key
del employee['age']

#print dict keys
print(employee.keys())
#print dict values
print(employee.items())

#loop trough keys
for key,value in employee.items():
    print(key,value)

