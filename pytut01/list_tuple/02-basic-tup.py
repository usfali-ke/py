# A tuple is a list that cannot change. Python refers to a value that cannot change as immutable. 
# So by definition, a tuple is an immutable list. Defined with () rather than []
rgb = ('red', 'green', 'blue')
print(rgb[0])
print(rgb[1])
print(rgb[2])

# Since a tuple is immutable, you cannot change its elements.
# rgb[0] = 'yellow'
'''
TypeError: 'tuple' object does not support item assignment
'''
# To define a tuple with one element, you need to include a trailing comma after the first element.
number = (3,)
print(type(number))

# If you exclude the trailing comma, the type of the numbers will be int
number = (3)
print(type(number))

# Even though you can’t change a tuple, you can assign a new tuple to a variable that references a tuple.
colors = ('red', 'green', 'blue')
print(colors)
colors = ('Cyan', 'Magenta', 'Yellow', 'black')
print(colors)

numbers = (23,5,2,89,100,342)
print(numbers)

