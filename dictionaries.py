my_dict={
    'name':'Michelle Kabue',
    'age':19,
    'gender':'Female',
    'city':'Nairobi'
}
print(my_dict)
print(type(my_dict))

#Accesing values in dict
print(my_dict['age'])
print(my_dict['city'])

#update amd add properties
my_dict['age']=30
print(my_dict)

#dictionary methods
#pop-removes the specified key
my_dict.pop('gender')
print(my_dict)

#popitem-removes the last added
my_dict.popitem()
print(my_dict)
