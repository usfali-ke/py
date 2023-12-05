# Python set comprehension to create a new set based on an existing one.

tags = {'Django', 'Pandas', 'Numpy'}
# To convert the tags in the set to another set of tags in lowercase, you may use the following for loop:

lower_tag = set()
for tag in tags:
    lower_tag.add(tag.lower())

print(tags)
print(lower_tag)

# Or you can use the built-in map() function with a lambda expression:
lower_tag2 = set()
lower_tag2 = map(lambda tag: tag.lower(), tags)
print(set(lower_tag2))

# To make the code more concise, Python provides you with the set comprehension syntax as follows:
tags = {'Python', 'Pandas', 'Numpy'}
lower_tag3 = set()
lower_tag3 = {tag.lower() for tag in tags}
print(lower_tag3)

# Python Set comprehension with an if clause example
# Suppose you want to convert all elements of the tags set to lowercase except for the Numpy.
new_tag = {tag.lower() for tag in tags if tag != "Numpy"}
print(new_tag)