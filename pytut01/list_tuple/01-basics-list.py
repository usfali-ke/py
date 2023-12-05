# A list is an ordered collection of items.
# The following shows an empty list:
empty_list = []
print(empty_list)

# Since a list often contains many items, it’s a good practice to name it using plural nouns e.g., numbers, colors, and shopping_carts
numbers = [1, 3, 2, 7, 9, 4, 9]
print(numbers)

colors = ['red', 'green', 'blue']
print(colors)

# Accessing elements in a list
# Since a list is an ordered collection, you can access its elements by indexes like this:
# list[index]
print(numbers[0])
print(numbers[4])

# The negative index allows you to access elements starting from the end of the list.
# The list[-1] returns the last element.
print(numbers[-1])

# Modifying elements in a list: list[index] = new_value
numbers[0] = 10
print(numbers)
# The following shows how to multiply the second element by 10:
numbers[1] = numbers[1]*10
print(numbers)

# Adding elements. 
# The append() method appends an element to the end of a list.
numbers.append(76)
print(numbers)

# The insert() method adds a new element at any position in the list.
numbers.insert(1, 100)
print(numbers)

# Removing elements from a list
del numbers[0]
print(numbers)

# The pop() method removes the last element from a list 
last = numbers.pop()
print(last)
print(numbers)

# To pop an element by its position, you use the pop() with the element’s index
second = numbers.pop(1)
print(second)
print(numbers)

# To remove an element by value, you use the remove() method. Note that the remove() method removes only the first element it encounters in the list.
numbers.remove(9)
print(numbers)

