# A Python set is an unordered list of immutable elements. It means:
# Elements in a set are unordered.
# Elements in a set are unique. A set doesn’t allow duplicate elements.
# Elements in a set cannot be changed. For example, they can be numbers, strings, and tuples, 
# but cannot be lists or dictionaries.
# To define a set in Python, you use the curly brace {}:
example = {'Python programming','Databases', 'Software design'}

# empty set
empty_set  = set()

skills = set()
if not skills:
    print('Empty sets are falsy')

# In fact, you can pass an iterable to the set() function to create a set.
skills = set(['Problem solving','Critical Thinking'])
print(skills)

# If an iterable has duplicate elements, the set() function will remove them.
characters = set("letters")
print(characters)

# To get the size/number of elements in a set, you use the built-in len() function
print(len(characters))

# Checking if an element is in a set
ratings = {1, 3, 4, 2, 8, 9}
rating = 4

if rating in ratings:
    print(f"{rating} found in the set")

# To negate the in operator, you use the not operator
rating = 89
if rating not in ratings:
    print(f"{rating} not found in the set")

# To add an element to a set, you use the add() method:
skills.add("Go Programming")
print(skills)

# To remove an element from a set, you use the remove()
skills.remove("Go Programming")
print(skills)

# If you remove an element that doesn’t exist in a set, you’ll get an error (KeyError).
# skills.remove('Java')
'''
KeyError: 'Java'
'''

# To avoid the error, you should use the in operator to check if an element is in the set before removing it:
if "Java" in skills:
    skills.remove("Java")

# To make it more convenient, the set has the discard() method that allows you to remove an element. And it doesn’t raise an error if the element is not in the list:
skills.discard('Java')

# To remove and return an element from a set, you use the pop() method.
# Since the elements in a set have no specific order, the pop() method removes an unspecified element from a set.
print(skills)
skill = skills.pop()
print(skills)

# To remove all elements from a set, you use the clear() method:
skills.clear()
print(skills)

# Frozen a set
# To make a set immutable, you use the built-in function called frozenset()
skills = {'Problem solving', 'Software design', 'Python programming'}
skills = frozenset(skills)

# After that, if you attempt to modify elements of the set, you’ll get an error:
# skills.add('Django')
'''
AttributeError: 'frozenset' object has no attribute 'add'
'''

# Looping through set elements
skills2 = {'Problem solving', 'Software design', 'Python programming'}
for skill in skills2:
    print(skill)

# To access the index of the current element inside the loop, you can use the built-in enumerate() function
for index, skill in enumerate(skills2):
    print(f"{index} - {skill}")

# By default, the index starts at zero. To change this, you pass the starting value to the second argument
for index, skill in enumerate(skills2, 1):
    print(f"{index} - {skill}")