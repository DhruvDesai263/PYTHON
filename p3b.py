#dictionary

s1 ={'name':'dhruv','id':'d22ce161','cgpa':7.5,'address':'river kent','hobbies':'cricket','languages':'c,c++'}
print(s1)

#update is use to add an key value pair in dictionary
s1.update({'cgpa':9.5})
print(s1)

#del is use to delete a pair of key value pair which id is [key]

del s1['hobbies']
print(s1)

#clear is use to clear the whole dictionary

s1.clear()

print(s1)

#new dictionary

s2={'Name':'Dhruv','ID':'D22CE161'}


#popitem removes the last key value pair from dictionary
s2.popitem()

print(s2)

s2.update({'ID':'D22CE161'})

#use to remove the pair which contain key "name"
s2.pop('Name')
print(s2)

s1.update({'Name':'Dhruv'})

#get returns the value of the key
print(s2.get('ID'))

