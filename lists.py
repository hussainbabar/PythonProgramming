#Python Lists & their methods
my_list = [1,2,3,4,5]
print(my_list)

#methods in Python
l1 = [1,2,3,4,5] #Append Method
l1.append(6)
print(l1) #Output: [1, 2, 3, 4, 5, 6]

#Extend Method
l2 = [6,7,8,9,10] #Original List
l1.extend(l2) #Extending l2 by l1
print(l1) #Output: [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]

#Insert Method
x = [1,2,3]  #Original List
x.insert(0,7) #Inserting 7 at index 0
print(x) #Output: [7, 1, 2, 3]

#Remove Method
y = [1,2,3,4,5]
y.remove(4) #Removing 4 from the list
print(y) #Output: [1, 2, 3, 5]

#Pop Method
z= [1,2,3,4,5]
z.pop(-1) #Popping element at index -1
print(z) #Output: [1, 2, 3, 4]


z= [1,2,3,4,5]
z.pop(1) #Popping element at index 1
print(z) #Output: [1, 3, 4, 5]

#Clear Method
a = [1,2,3,4,4]
a.clear() #Clearing the list
print(a) #Output: []

#Index Method

b = [1,6,7,4]
#Finding index of 6
print(b.index(6)) #Output: [1, 6, 7, 4]

#count Method
c= ['red','blue','green','blue','blue']
print(c.count('blue')) #Output: 3

#sort Method
d= ['black','blue','green','white','yellow']
print(d.sort()) #Sorting the list)

e= ['green','black','blue','white','yellow']
e.sort() #Sorting the list
print(e) #Output: ['black', 'blue', 'green', 'white', 'yellow']

#2nd Way to sort

my_sort = ["banana","apple","orange","mango"]
print(sorted(my_sort)) #Output: ['apple', 'banana', 'mango', 'orange']

# When to use what?
# Use sort() → when you want to permanently change the list
# Use sorted() → when you want a new sorted list without changing original

#Reverse Method

s = ["key","apple","mango","banana"]
s.reverse() #Reversing the list
print(s) #Output: ['banana', 'mango', 'apple', 'key']

#copy Method


original = [1,2,3,4,5]
new_list = original.copy() #Copying original list to new_list
print(new_list) #Output: [1, 2, 3, 4, 5]    

#2nd way to copy a list
original = [1,2,3,4,5]
copy_list = [12,13,14,15]
new_list1 =  original + copy_list #Concatenating two lists
print(new_list1) #Output: [1, 2, 3, 4, 5, 12, 13, 14, 15]   

#3rd way to copy a list
originalone = [1,2,3,4,5]
new_list2 = originalone[:] #Using Slicing to copy a list
print(new_list2) #Output: [1, 2, 3, 4, 5]

#4th way to copy a list
originaltwo = [1,2,3,4,5]
new_list3 = list(originaltwo) #Using list() method to copy a list
print(new_list3) #Output: [1, 2, 3, 4, 5]   
