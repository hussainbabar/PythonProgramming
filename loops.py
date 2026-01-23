#Exercise 1: Print first 10 natural numbers using while loop
i =1
while i <= 10:
    print(i)
    i += 1 

# print number pattern 

# Decide the row count. 

row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i +1):
        print(j, end=" ")
    print(" ")

#Write a Python program to print the reverse number pattern using a for loop.

rows = 5 

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

#Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)

#method 2 
n = int(input("Enter number "))
x = sum(range(1, n+1,1))
print(x)

#Print multiplication table of a given number
n = 2
for i in range(1, 11):
    product = n *i
    print(product)

#Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    if i <= 150 and i % 5 ==0:
        print(i)

#Count the total number of digits in a number
given_numner =  75869
lis1 = list(str(given_numner))
print(lis1)
print(len(lis1))

#Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
rev_list = []

for i in list1[::-1]:
    rev_list.append(i)

print(rev_list)

#Display numbers from -10 to -1 using for loop

for i in range(-10, 0, 1):
    print(i)


#Display a message “Done” after the successful execution of the for loop

for i in range(1, 11):
    print(i)
else:
    print("Done")
    
# Print all prime numbers within a range

start = 25
end = 50

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
