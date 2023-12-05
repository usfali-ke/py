# Python Iterables
# In Python, an iterable is an object that includes zero, one, or many elements. An iterable has the ability to return its elements one at a time.
# Because of this feature, you can use a for loop to iterate over an iterable.
# Examples - range, string, list, tuple, etc.
print("[+] Learning Python Iterables")
for i in range(4):
    print(i)

# An iterable can be iterated over. And an iterator is the agent that performs the iteration.
# To get an iterator from an iterable, you use the iter() function
colors = ['red', 'green', 'blue']
print(colors)
colors_iter = iter(colors)

# Every time, you call the next() function, it returns the next element in the iterable.
color = next(colors_iter)
print(color)
color = next(colors_iter)
print(color)
color = next(colors_iter)
print(color)

# If there isn’t any more element and you call the next() function, you’ll get an exception.
# color = next(colors_iter)
# print(color)
'''
StopIteration
'''

# Since you can iterate over an iterator, the iterator is also an iterable object
print("\nLooping over the iterable object...")
iterator = iter(colors)
for color in iterator:
    print(color)

# Python map() function with lists.
# When working with a list (or a tuple), you often need to transform the elements of the list 
# and return a new list that contains the transformed element.
print("\n[+] Python map() function with lists")
bonuses = [100, 200, 300]
# Doubling the bonuses
new_bonuses = []
for bonus in bonuses:
    new_bonuses.append(bonus * 2)

print(new_bonuses)

# Python provides a nicer way to do this kind of task by using the map() built-in function.
# The map() function iterates over all elements in a list (or a tuple), applies a function to each, and returns a new iterator of the new elements.
# iterator = map(fn, list)
# fn is the name of the function that will call on each element of the list.
# In fact, you can pass any iterable to the map() function, not just a list or tuple.

def double(bonus):
    return bonus * 2

iterator = map(double, bonuses)
print(list(iterator))

# Or you make this code more concise by using a lambda expression like this:
iterator = map(lambda bonus: bonus *2, bonuses)
print(list(iterator))

# Using the Python map() function for a list of strings
names = ['david', 'peter', 'jenifer']
print(names)
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))

# Using the Python map() function to a list of tuples
# calculate the tax amount for each product with a 10% tax and add as third column
carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]
tax = 0.1
new_carts = map(lambda item: [item[0], item[1], item[1]*tax], carts)
print(carts)
print(list(new_carts))
