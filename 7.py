#Write a program to create a dictionary and demonstrate dictionary methods and iteration.

dic={
    'name': 'Palak',
    'age':'21',
    'city':'rajkot'}

print(dic)

#print specific key
print(dic["city"])

#change age

dic["age"]= 22
print(dic)

#add pair

dic["Contact"]='9909451909'
dic["Gender"]= 'Female'
print(dic)

#pop elements

dic.pop("age")
print(dic)
