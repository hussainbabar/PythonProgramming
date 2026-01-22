# Python Sets

s1 = {1, 2, 3, 4, 5}
print(s1)  # Output: {1, 2, 3, 4, 5}
print(type(s1))  # Output: <class 'set'>

#Count Menthod
s2 = {1, 2, 2, 3, 4, 5}
print(s2)  # Output: {1, 2, 3, 4, 5} (duplicates are removed)

# Count Method
# Sets do not have a count method because they do not allow duplicates. 
# Instead, you can check for membership using the 'in' keyword.
print(2 in s2)  # Output: True
print(6 in s2)  # Output: False 

# Adding Elements
s3 = {1, 2, 3}
s3.add(4)
print(s3)  # Output: {1, 2, 3, 4}

s = {1,3}
s.add(5)
print(s)
# Update Elements 
s4 = {1, 2, 3}
s4.update([3,4,5,6])
print(s4)

# Removing Elements
s5 = {1, 2, 3, 4, 5}
s5.remove(3)
print(s5)  # Output: {1, 2, 4, 5}

#discard method
s6 = {1, 2, 3, 4, 5}
s6.discard(2)
print(s6)

s6.discard(10)
print(s6)

# pop method
s7 = {1, 2, 3, 4, 5}
s7.pop()
print(s7)
s7.pop()
print(s7)

# clear method
s8 = {1, 2, 3, 4, 5}
s8.clear()
print(s8)  # Output: set()  

# Set Operations
s9 = {1, 2, 3}
s10 = {3, 4, 5}
print(s9.union(s10))   # Output: {1, 2, 3, 4, 5}
print(s9 | s10)
print(s10.union(s9))

#intersection
s11 = {1, 2, 3}
s12 = {3, 4, 5}
print(s11.intersection(s12))
print(s11 & s12)

#difference
s13 = {1, 2, 3}
s14 = {3, 4, 5}
print(s13.difference(s14))
print(s13 - s14)

#symmetric difference
s15 = {1, 2, 3}
s16 = {3, 4, 5}
print(s15.symmetric_difference(s16))
print( s15 ^ s16)

#superset
s17 = {1, 2, 3, 4, 5}
s18 = {2, 3, 4}
print(s17.issuperset(s18))
print(s18.issuperset(s17))

#subset
s19 = {1, 2, 3, 4, 5}
s20 = {2, 3, 4}
print(s20.issubset(s19))
print(s19.issubset(s20))

#isdisjoint
s21 = {1, 2, 3}
s22 = {4, 5, 6}
print(s21.isdisjoint(s22))

s21 = {1, 2, 3}
s22 = {1, 2, 3}

print(s21.isdisjoint(s22))

# Looping through a Set
s23 = {10, 20, 30, 40, 50}
for i in s23:
    print(i)   
