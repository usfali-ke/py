# learn about Python list slice and how to use it to manipulate lists effectively.
# Lists support the slice notation that allows you to get a sublist from a list:
# sub_list = list[begin: end: step]
# In this syntax, the begin, end, and step arguments must be valid indexes. And they’re all optional.
# The begin index defaults to zero. The end index defaults to the length of the list. And the step index defaults to 1.
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(colors)
# The begin index is 1, so the slice starts from the 'orange' color. The end index is 4, therefore, the last element of the slice is 'green'.
sub_colors = colors[1:4]
print(sub_colors)

# returns a list that includes the first three elements from the colors list:
# Notice that the colors[:3] is equivalent to the color[0:3].
sub_colors = colors[:3]
print(sub_colors)

# the following returns a list that includes the last 3 elements of the colors list:
sub_colors = colors[-3:]
print(sub_colors)

# Uses the step to return a sublist that includes every 2nd element of the colors list:
sub_colors = colors[::2]
print(sub_colors)

# Using Python List slice to reverse a list
sub_colors = colors[::-1]
print(sub_colors)

# Using Python List slice to substitute part of a list
colors[0:2] = ["black", "white"]
print(colors)

# Using Python List slice to partially replace and resize a list
# Below uses the list slice to replace the first and second elements with the new ones 
# and also add a new element to the list:
print(f"The list has {len(colors)} elements")

colors[0:2] = ["black", "white", "pink"]
print(colors)
print(f"The list has {len(colors)} elements")

# Using Python list slice to delete elements
# Below uses the list slice to delete the 3rd, 4th, and 5th elements from the colors list:
del colors[2:5]
print(colors)

# However, Python provides a better way to do this. It’s called sequence unpacking.
# Basically, you can assign elements of a list (and also a tuple) to multiple variables.
colors = ['red', 'blue', 'green']
# This statement assigns the first, second, and third elements of the colors list to the red, blue, and green variables.
# If you use a fewer number of variables on the left side, you’ll get an error.
red, blue, gren = colors
print(red)

# If you want to unpack the first few elements of a list and don’t care about the other elements, you can:
# First, unpack the needed elements to variables.
# Second, pack the leftover elements into a new list and assign it to another variable.
# By putting the asterisk (*) in front of a variable name, you’ll pack the leftover elements into a list and assign them to a variable.
colors = ['red', 'blue', 'green', "black", "white"]
red, blue, *others = colors
print(red)
print(blue)
print(others)

# Using Python for loop to iterate over a list
# To iterate over a list, you use the for loop statement as follows:
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
print(cities)
for city in cities:
    print(city)

# Sometimes, you may want to access indexes of elements inside the loop. In these cases, you can use the enumerate() function.
# It returns a tuple that contains the current index and element of the list.
for item in enumerate(cities):
    print(item)

# To access the index, you can unpack the tuple within the for loop statement like this:
for index, city in enumerate(cities):
    print(f"{index} - {city}")

# The enumerate() function allows you to specify the starting index which defaults to zero.
for index, city in enumerate(cities, 1):
    print(f"{index} - {city}")

# To find the index of an element in a list, you use the index() function.
result = cities.index('Mumbai')
print(result)

# However, if you attempt to find an element that doesn’t exist in the list using the index() function, you’ll get an error.
# result = cities.index('Nairobi')
# print(result)
'''
ValueError: 'Nairobi' is not in list
'''

# To fix this issue, you need to use the in operator.
city = "Nairobi"
if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}")
else:
    print(f"The {city} does not exist in our cities list")
    