# Python Tuple Data Type & its methods
#characteristics of Tuple
#1. Ordered
#2. Immutable
#3. Allow Duplicates 
#Creating a Tuple
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))  #Output: <class 'tuple'>

#Indexing and Slicing
print(my_tuple[1])  # Output: 2
print(my_tuple[-1]) # Output: 5

#slicing

my_tuple = (1,2,3,4,5)
print(my_tuple[0:])
print(my_tuple[0:3])
print(my_tuple[-3:])
print(my_tuple[:-1])
print(my_tuple[-1:])

#Different ways to create Tuple
#1st way
t1 = (1,2,3,4,5)
print(t1)       #Output: (1, 2, 3, 4, 5)
#2nd way
t2 = 1,2,3,4,5
print(t2)    #Output: (1, 2, 3, 4, 5)
#3rd way
t3 = (1,)
print(t3)    #Output: (1,)
#4th way
t4 = tuple([1,2,3,4,5])
print(t4)    #Output: (1, 2, 3, 4, 5)       

#Tuple Methods
#1st Method: count()
t5 = (1,2,3,4,5,2,2)
print(t5.count(2))   #Output: 3         
#2nd Method: index()
t6 = (1,2,3,4,5)
print(t6.index(3))   #Output: 2
#Tuple Unpacking
t7 = (1,2,3)
a,b,c = t7
print(a)   #Output: 1
print(b)   #Output: 2
print(c)   #Output: 3
#Looping through a Tuple
t8 = (10,20,30,40,50)
for i in t8:
    print(i)        
#Tuple Concatenation
t9 = (1,2,3)
t10 = (4,5,6)
t11 = t9 + t10
print(t11)   #Output: (1, 2, 3, 4, 5, 6)
#Tuple Repetition
t12 = (1,2,3)
t13 = t12 * 3
print(t13)   #Output: (1, 2, 3, 1   , 2, 3, 1, 2, 3)
#Membership Testing
t14 = ('apple','banana','cherry')
print('apple' in t14)      #Output: True                        
print('grape' not in t14)   #Output: True
#Nested Tuples
t15 = ((1,2),(3,4),(5,6))
print(t15[0])      #Output: (1, 2)
print(t15[1])      #Output: (3, 4)
print(t15[2])      #Output: (5, 6)
print(t15[0][1])   #Output: 2
print(t15[2][0])   #Output: 5           
print(t15[-1])     #Output: (5, 6)
print(t15[-3][-1]) #Output: 2
#Tuple to List Conversion
t16 = (1,2,3,4,5)
list_from_tuple = list(t16)
print(list_from_tuple)   #Output: [1, 2, 3, 4, 5]
#List to Tuple Conversion
list1 = [1,2,3,4,5]
tuple_from_list = tuple(list1)
print(tuple_from_list)   #Output: (1, 2, 3, 4, 5)       
#Finding Length of Tuple
t17 = (1,2,3,4,5)
print(len(t17))   #Output: 5    
#Finding Maximum and Minimum in Tuple
t18 = (10,5,8,20,3)     
print(max(t18))   #Output: 20
print(min(t18))   #Output: 3    
#Summation of Tuple Elements        
t19 = (1,2,3,4,5)       
print(sum(t19))   #Output: 15
#Tuple Immutability
t20 = (1,2,3)
# t20[0] = 10  # This will raise a TypeError
print(t20)   #Output: (1, 2, 3) 