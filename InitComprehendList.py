#Examples on comprehending lists

#by declaration
nums=[1,2,3]

l=[]

#by appending
for x in nums:
   l.append(x)

#one more way
l1=[x for x in nums]

#one more way
l1=[x+1 for x in nums]


#by using lambda mapping
l1=map(lambda x:x+2,nums)



l1=[x for x in nums if x>2]

#by using lambda filter
l1=filter(lambda  x: x>2,nums)

for x in l1:
    print(x)

people=['john','luke','mathew']
gospel=['one','two','three']


#comprehending dictionary
l1=[(x,y) for x in people for y in gospel]

#tuple
l1=zip(people,gospel)

for x in l1:
    print(x)

bible={}
#comprehending dictionary
for people,gospel in zip(people,gospel):
    bible[people]=gospel

print("-------------")

for key in bible.keys():
    print(key,bible.get(key))


#comprehend SET
s={n for n in nums}

