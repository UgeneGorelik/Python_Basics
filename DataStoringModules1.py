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

#build Map
def buildMap(s):
    the_map = {}
    for char in s:
        if char not in the_map:
            the_map[char] = 1
        else:
            the_map[char] += 1

    return the_map

#sort Dictionary
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=lambda t: t[1])

#max and min values in dict
print(max((value, key) for key, value in x.items())[1])

print(min((value, key) for key, value in x.items())[1])
