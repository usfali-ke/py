# Python filter() function
# Sometimes, you need to iterate over elements of a list and select some of them based on specified criteria.
scores = [70, 60, 81, 90, 50, 85]
filtered = []
for score in scores:
    if score > 80:
        filtered.append(score)

print(scores)
print(filtered)

# Python has a built-in function called filter() that allows you to filter a list (or a tuple) in a more beautiful way.
# filter(fn, list)
# The filter() function iterates over the elements of the list and applies the fn() function to each element. It returns an iterator for the elements where the fn() returns True.
# In fact, you can pass any iterable to the second argument of the filter() function, not just a list.

filtered2 = filter(lambda score: score > 80, scores)
print(list(filtered2))

# Since the filter() function returns an iterator, you can use a for loop to iterate over it. 
# Or you can use the list() function to convert the iterator to a list.

# Using the Python filter() function to filter a list of tuples
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

# To get all the countries whose populations are greater than 300 million
updated_pop = filter(lambda item: item[1] > 300000000, countries)
print(list(updated_pop))

# Python reduce() function to reduce a list into a single value.
scores = [75, 65, 80, 95, 50]

# to calculate the sum of all elements in the scores list, you can use a for loop like this:
total = 0
for score in scores:
    total += score

print(total)

# In above example, we have reduced the whole list into a single value, which is the sum of all elements from the list.

# Python offers a function called reduce() that allows you to reduce a list in a more concise way.
# reduce(fn,list)
# the reduce() isn’t a built-in function in Python. In fact, the reduce() function belongs to the functools module.
# The reduce() function applies the fn function of two arguments cumulatively to the items of the list, from left to right, 
# to reduce the list into a single value.
from functools import reduce

def sum(a, b):
    print(f"a={a},b={b}, {a}+{b}={a+b}")
    return a + b

total2 = 0
total2 = reduce(sum, scores)
print(total2)

# To make the code more concise, you can use a lambda expression instead of defining the sum() function:
print("Using lambda...")
total3 = 0
total3 = reduce(lambda a, b: a + b, scores)
print(total3)