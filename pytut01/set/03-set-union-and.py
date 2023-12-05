# Python Set Union
# The union of two sets returns a new set that contains distinct elements from both sets.
print("\nLearning Python set Union")
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

# s3 = s1.union(s2)
s3 = s1 | s2
print(s3)

# the union() method accepts one or more iterables, converts the iterables to sets, and performs the union.
# However, the union operator (|) only allows sets, not iterables like the union() method.

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)
print(ratings)
# The following example causes an error:
# ratings = rates | ranks
'''
TypeError: unsupported operand type(s) for |: 'set' and 'list'
'''
print("\nLearning Python set intersection()")
# Python set intersection() method or set intersection operator (&) to intersect two or more sets:
# new_set = set1.intersection(set2, set3)
# new_set = set1 & set2 & set3

# When intersecting two or more sets, you’ll get a new set consisting of elements that exist in all sets.

# Using Python set intersection() method to intersect two or more sets
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.intersection(s2)
print(s)

# Using Python set intersection (&) operator to intersect two or more sets
s1 = {'Python', 'Node', 'C++'}
s2 = {'C#', 'Node', 'C++'}

s = s1 & s2

print(s)

# The set intersection operator only allows sets, while the set intersection() method can accept any iterables, like strings, lists, and dictionaries.
# If you pass iterables to the intersection() method, it’ll convert the iterables to set before intersecting them.
# However, the set intersection operator (&) will raise an error if you use it with iterables.

# Python Set difference
# The difference between the two sets results in a new set that has elements from the first set 
# which aren’t present in the second set.
# use the set difference() method or set difference operator (-) to find the difference between sets.

# Using Python Set difference() method to find the difference between sets
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.difference(s2)

print(s)

# Using Python set difference operator (-) to find the difference between sets
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2 - s1

print(s)

# The set difference() method can accept one or more iterables (e.g., strings, lists, dictionaries) 
# while the set difference operator (-) only allows sets.
# When you pass iterables to the set difference() method, it’ll convert the iterables to sets before 
# performing the difference operation.
# However, if you use the set difference operator (-) with iterables, you’ll get an error
scores = {7, 8, 9}
numbers = [9, 10]
# new_scores = scores - numbers
'''
TypeError: unsupported operand type(s) for -: 'set' and 'list'
'''
# print(new_scores)

print("\nLearning Python Symmetric Difference")
# Python Symmetric Difference
# The symmetric difference between two sets is a set of elements that are in either set, 
# but not in their intersection.
# Suppose that you have the following s1 and s2 sets:
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

# The symmetric difference of the s1 and s2 sets returns in the following set:
# {'C#', 'Python'}
# elements are either in s1 or s2 set, but not in their intersection.

# you can find the symmetric difference of two or more sets by using the set symmetric_difference() method or the symmetric difference operator (^)

s = s1.symmetric_difference(s2)
# s = s1 ^ s2
print(s)

# The symmetric_difference() method accepts one or more iterables that can be strings, lists, or dictionaries.
# If the iterables aren’t sets, the method will convert them to sets before returning the symmetric difference of them.

# However, the symmetric difference operator (^) only applies to sets. If you use it with the iterables which aren’t sets, you’ll get an error

print("\nLearning Python issubset()")
# use the Python issubset() method to check if a set is a subset of another set.
# Suppose that you have two sets A and B. Set A is a subset of set B if all elements of A are also elements of B. Then, set B is a superset of set A.
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}
print(scores.issubset(numbers))

# By definition, a set is also a subset of itself. 
numbers = {1, 2, 3, 4, 5}
print(numbers.issubset(numbers))

print(numbers.issubset(scores)) # False

# Using subset operators
# Besides using the issubset() method, you can use the subset operator (<=) to check if a set is a subset of another set
result = scores <= numbers
print(result)

result = numbers <= numbers
print(result)

# The proper subset operator (<) check if the set_a is a proper subset of the set_b
result = scores < numbers
print(result)  # True

result = numbers < numbers
print(result) # False

# Python issuperset
print("\nLearning Python issuperset")
# Give sets A and B. Set A is a superset of set B if all elements of set B are elements of set A.
# n Python, you use the set issuperset() method to check if a set is a superset of another set:
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers.issuperset(scores)
print(result) # True

# A set is also a superset of itself.
result = numbers.issuperset(numbers)
print(result) # True

# Using superset operators
# The >= operator determines if a set is a superset of another set:
result = numbers >= scores
print(result) # True

# To check if a set is a proper superset of another set, you use the > operator
result = numbers > scores
print(result) # True

result = numbers > numbers
print(result) # False

# Python Disjoint Sets
print("\nLearning Python Disjoint Sets")
# Two sets are disjoint when they have no elements in common. In other words, two disjoint sets are sets whose intersection is an empty set.
# For example, the {1,3,5} and {2,4,6} sets are disjoint because they have no common elements.
# In Python, you use the Set isdisjoint() method to check if two sets are disjoint or not:
odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}

result = odd_numbers.isdisjoint(even_numbers)
print(result)

# The following example passes a list to the isdisjoint() method instead of a set:
letters = {'A', 'B', 'C'}
result = letters.isdisjoint([1, 2, 3])
print(result) # True