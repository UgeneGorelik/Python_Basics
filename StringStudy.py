#Basic working with String examples

#create string
message='hi world'

#print string
print(message)

#print lenght of string
print(len(message))

#print string at index1
print(message[0])

#print string from index 0 to index 1
print(message[0:1])

#count appearnces
print(message.count('i'))

#find index of
print(message.find('hi'))

#replace at index
message1=message.replace('hi','bye')

#concat stings
message3=message+" " +message1

print(message3)

#format string
message4 ='{},{}'.format('oh','yeah')

print(message4)

#print all available commads for str
print((help(str)))





