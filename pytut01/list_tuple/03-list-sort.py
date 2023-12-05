numbers = [1, 3, 2, 7, 9, 4, 9]
print(numbers)
# To sort a list, you use the sort() method:
numbers.sort()
print(numbers)

# To sort elements from higher to lower, you pass the reverse=True
numbers.sort(reverse=True)
print(numbers)

# If a list contains strings, the sort() method sorts the string elements alphabetically.
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
print(guests)
guests.sort()
print(guests)

# Using the Python List sort() method to sort a list of tuples
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]
print(companies)
# to sort the companies list by revenue from highest to lowest.
# First, specify a sort key and pass it to the sort() method. 
# To define a sort key, you create a function that accepts a tuple and returns the element 
# that you want to sort by, in below case, third element:
def sort_key(company):
    return company[2]

# Second, pass the sort_key function to the sort() method:
companies.sort(key=sort_key, reverse=True)

# The sort() method will use the value returned by the sort_key() function for the comparisons.
print(companies)

# Using lambda expression
# To make it more concise, Python allows you to define a function without a name with the following syntax:
# lambda arguments: expression
# A function without a name is called an anonymous function. And this syntax is called a lambda expression.
# Technically, it’s equivalent to the following function:
# def name(arguments):
#     return expression
companies.sort(key=lambda company: company[2], reverse=True)
print(companies)

# The sort() method sorts a list in place. In other words, it changes the order of elements in the original list.
# To return the new sorted list from the original list, you use the sorted() function:
guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guests = sorted(guests)
print(guests)
print(sorted_guests)
# sort the guests list in the reverse alphabetical order:
sorted_guests_rev = sorted(guests, reverse=True)
print(sorted_guests_rev)

# Using Python sorted() function to sort a list of numbers
scores = [5, 7, 4, 6, 9, 8]
sorted_scores = sorted(scores)
print(scores)
print(sorted_scores)
# reversed
sorted_scores_rev = sorted(scores, reverse=True)
print(sorted_scores_rev)

