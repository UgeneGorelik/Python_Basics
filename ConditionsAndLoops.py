#basic examples of loops and conditions

#Conditions




#example of if elif else

fat_food= 'Good'

if fat_food == 'Basd':
    print('that sucks')
elif fat_food == 'not tasty':
    print('yep')
else:
    print('hopefasdasdully')

git push --set-upstream origin tst_branch -o merge_request.create


x=1
y=2
#check if same object in memory

if x is not y:
    print('not correct')

#and or example

x=y
if x==y and y==2 or x==1:
    print('tree of the conditions true')


#print the inner id of variable
print(id(x))

print(id(y))


#good check if list is empty
cond={}

if not cond:
    print("if dict is empty its false")

#Loops


numbers=[1,2,3]

for x in numbers:
    print(x)

for x in numbers:
    print(x)
    if x == 2:
        break


#prints all combinations
for x in  numbers:
    for y in 'abc':
        print(x,y)

for i in range(2,10):
    print(i)

x=0


#while examle
while x < 5:
    print('looping man i am looping OKAY?')
    x+=1





