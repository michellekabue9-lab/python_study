my_list=['Mike','Jane','Mary',100,200,300, True,False]
#remove-remove items with specified value
my_list.remove(100)
print(my_list)

#pop-Remove element at specified position.
my_list.pop(0)
print(my_list)

#qppend-add items at the end of the list
my_list.append('Joy')
print(my_list)

#insert-adds items at specific index
my_list.insert(1,'Miracle')
print(my_list)
my_list.insert(5,1000)
print(my_list)

#task
lst=[100,200,300,['Mary','Kim',[1000,2000,3000]], 40,50,60]
#add 70 at the end of the list

lst.append(70)
print(lst)

#add jane betwin mary and kim
lst[3].insert(1,'Jane')
print(lst)

#add 1500 btn 1000 and 2000
lst[3] [3].insert(1,1500)
print(lst)

#delete 2000
lst[3][3].remove(2000)
print(lst)

#count-count the number of appearance
lst2['Mike','Mary','Jane']