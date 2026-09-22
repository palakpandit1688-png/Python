#Write a program to explain mutable and immutable objects in Python.
# immutable objects

#integer:
a='10'
print(a)

a='20'
print('after change:',a)

#float:
b='20.50'
print(b)

#string
str='Palak'
print(str)

#tuple
tuple=(10,20,30)
print(tuple)

#mutable object

#List:

list=[1,2,3,4,'A','B']
print(list)
print(list[:2])
print(list[2:5])

list.append('Palak')
print('After append:',list)

list.remove(1)
print('After Remove :',list)

list.pop()
print('After pop:',list)

#tuple

tuple=(10,20,30,40,50)
print(tuple)
print(tuple[:4])
print(tuple[-2])

#tuple.append('60','70','80')
#print('After append :',tuple)

#tuple.remove(60)
#print('After Remove :',tuple)

#tuple.pop()
#print('after pop:',tuple)

#tuple.reverse()
#print('after reverse:',tuple)


#set :

set={100,200,300,400,500}
print(set)

set.add(600)
print(set)

set.update([600,700,800])
print(set)

set.pop()
print(set)

#set.delete(600)
#print(set)
