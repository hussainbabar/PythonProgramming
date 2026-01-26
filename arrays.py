import array as arr
n = arr.array(("i"),[1,2,3,4,5])
print(n)

print(n[3])

print(n[1:4])

n.append(7)

print(n)

n.extend([8,9,10])
print(n)

n[7] = 6
print(n)


n.remove(7)
print(n)

n.pop(3)
print(n)

n.insert(23,24)
print(n)

n.insert(0,45)
print(n)


# Insert an Item Before the Second Element in an Array

a = arr.array(("i"),[1,2,3,4,5,])

a.insert(1,7)

print(a)

#Remove a Specified Item Using the Index of an Array

b= arr.array(("i"),[1,2,3,4,5,6])

b.pop(0)

print(b)

# Convert an Array to an Ordinary List with the Same Items
c = arr.array(("i"),[11,12,13,14,15])
d = c.tolist()
print(d)
print(type(d))

#Check if an Array Contains Any Duplicate Elements
e = arr.array(("i"),[1,2,3,4,5,1,2,3])
duplicates = set() # define a set to store duplicates
seen = set()    #define two sets
for item in e:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print(duplicates)

#Remove All Duplicate Elements from an Array
f = arr.array(("i"),[1,2,3,4,5,1,2,3])
unique_arr = []
for i in f:
    if i not in unique_arr:
        unique_arr.append(i)
print(unique_arr)

#Find Missing Number in an Array of Numbers Between 10 and 20
g = arr.array(("i"),[10,11,12,13,14,15,16,18,19,20])
for i in range(10,21):
    if i not in g:
        print("Missing number is:",i)
        break
