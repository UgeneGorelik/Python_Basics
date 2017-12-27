#basic knowlege of working with files

#open file to read
f = open('example.txt','r')

#print file name
print(f.name)

#print the mode we working with the file
print(f.mode)

#close file and sumbit changes
f.close()

#open and close automatically in one function
with open('example.txt', 'r') as f:
        data=f.read()
        print(data)

#read all lines into list
with open('example.txt', 'r') as f:
    data = f.readlines()
    print(data)

#read one line into list
with open('example.txt', 'r') as f:
    data = f.readline()
    print(data)

print("__________")

#print all lines in file
with open('example.txt', 'r') as f:
   for x in f:
       print(x)

#read a chunk of data
with open('example.txt', 'r') as f:
   data=f.read(6)
   print(data)

#rad a chunk of data and set string to see when finished
with open('example.txt', 'r') as f:
   data=f.read(2)
   print(data,end="Thats ALL FOLKS")



#seek rewinds the place to index
with open('example.txt', 'r') as f:
   data=f.read(2)
   print(data,end="Thats ALL FOLKS")
   f.seek(0)
   data = f.read(2)
   print(data, end="Read from start")

#write into file
with open('example1.txt','w') as f:
    f.write('Hayad od roshemet')