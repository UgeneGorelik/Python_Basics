#Basic Data storing modules


#Lists

#init List
applications =['TC','RLC','INV']

print(applications)

#print member at index 0
print(applications[0])

#print member at index 1 from end
print(applications[-1])

print(applications[0:3])


#append
applications.append('OFCA')


#insert at index
applications.insert(1,'CORE')

#pop value into variable
taken=applications.pop()

print(taken)

numbers=[1,2,3,4,0]

#sort list
numbers.sort()

print(numbers)

#sort in reverse
rev_numbers=numbers.sort(reverse=True)

print(numbers)

print(max(numbers))

#see at what index
print(applications.index('INV'))

#check if list contains
print('OFCA' in applications)

for x in applications:
    print(x)

#create string divided by ,
app=', '.join(applications)

print(app)

#create list from string if string separated by ,
app_new=app.split(',')

print(app_new)

#Tuples are list you cant modify

tu1=('A','B')

#Sets can hold only unique vales

set_app={'OFCA','RLC','RLC'}

set_app2={'OFCA','RLC','TC'}

print(app)

#check what members intersect
print(set_app.intersection(set_app2))

#check what members are diffreent
print(set_app.difference(set_app2))

#see what is the union
print(set_app.union(set_app2))


#Sorting

l=[1,2,3,4,5]

l1=sorted(l)

l.sort()

print(l1)

l=[-1,-2,5,6]

l2=sorted(l,key=abs)

print(l2)

