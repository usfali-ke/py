# Python List comprehensions that allow you to create a new list from an existing one.
# suppose that you have a list of five numbers and you want to get a list of squares based on this numbers list
# The straightforward way is to use a for loop:
numbers = [1, 2, 3, 4, 5]

sq_numbers = []
for number in numbers:
    # number*number same as number**2
    sq_numbers.append(number**2)

print(numbers)
print(sq_numbers)

# To make the code more concise, you can use the built-in map() function with a lambda expression:
sq_numbers2 = map(lambda number: number**2, numbers)
print(list(sq_numbers2))

# Both the for loop and map() function can help you create a new list based on an existing one. But the code isn’t really concise and beautiful.
# To help you create a list based on the transformation of elements of an existing list, Python provides a feature called list comprehensions.
square = [number**2 for number in numbers]
print(square)
# A list comprehension consists of the following parts:
# An input list (numbers)
# A variable that represents the elements of the list (number)
# An output expression (number**2) that returns the elements of the output list from the elements of the input list.

# Python list comprehension with if condition
# To get a list of mountains where the height is greater than 8600 meters, 
# you can use a for loop or the filter() function with a lambda expression like this:
mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]
highest = filter(lambda height: height[1] > 8600, mountains)
print(list(highest))

# This list comprehension allows you to replace the filter() with a lambda expression:
highest2 = [m for m in mountains if m[1] > 8600]
print(highest2)