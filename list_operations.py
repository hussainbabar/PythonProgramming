#list Operations
#Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Concatenated List:", combined_list)  # Output: [1, 2, 3, 4, 5, 6]    

#Repetition
l1 = [1,2,3]
repeated_list = l1 * 3
print("Repeated List:", repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

#membership Testing
my_list = ['apple', 'banana', 'cherry']
print('apple'in my_list)
print('grape' not in my_list)

#Iteration
l3 = [10,20,30,40,50]
for i in l3:
    print(i)

#Summation
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("Sum of List Elements:", total)  # Output: 15 

#maximum and Minimum
values = [10, 5, 8, 20, 3]
max_value = max(values)
print("Maximum Value:", max_value)  # Output: 20
min_value = min(values)
print("Minimum Value:", min_value)  # Output: 3 

#nested Lists
x1 = [[1,2],[3,4],[4,5]]
print(x1[0])
print(x1[1])
print(x1[2])
print(x1[0][1])
print(x1[2][0])
print(x1[-1])
print(x1[-3][-1])


