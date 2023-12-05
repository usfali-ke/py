# The following example defines an empty dictionary:
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# The following example defines a dictionary with some key-value pairs:
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

# Accessing dict
# To access a value associated with a key, you place the key inside square brackets:
print(person['first_name'])
print(person['last_name'])

# If you attempt to access a key that doesn’t exist, you’ll get an error. 
# ssn = person['ssn']
'''
Traceback (most recent call last):
  File "/home/alien/Documents/python/pytut01/dict/01-basics.py", line 21, in <module>
    ssn = person['ssn']
          ~~~~~~^^^^^^^
KeyError: 'ssn'
'''

# To avoid this error, you can use the get() method of the dictionary:
ssn = person.get('ssn')
print(ssn)

# The get() method also returns a default value when the key doesn’t exist by passing the default value to its second argument.
ssn = person.get('ssn', '000-00-0000')
print(ssn)

# Adding new key-value pairs
# The following example adds a new key-value pair to the person dictionary:
person["gender"] = "Female"
print(person)

# Modifying values in a key-value pair
person["gender"] = "Male"
print(person)

# To remove a key-value pair by a key, you use the del statement:
del person["active"]
print(person)

# Looping through a dictionary
# Python dictionary provides a method called items() that returns an object which contains a list of key-value pairs as tuples in a list.
print(person.items())

# o iterate over all key-value pairs in a dictionary, you use a for loop with two variable key and value to unpack each tuple of the list:
for key, value in person.items():
    print(f"{key}: {value}")

# Looping through all the keys in a dictionary
for key in person.keys():
    print(key)

# In fact, looping through all keys is the default behavior when looping through a dictionary. Therefore, you don’t need to use the keys() method.
# Below will also work/okay
for key in person:
    print(key)

# Looping through all the values in a dictionary
for v in person.values():
    print(v)

# Remove the element with specified key
person.pop("last_name")
print(person)

# Removes the last inserted key-value pair
person["address"] = "P.O Box 30888"
print(person)
person.popitem()
print(person)

d = {"age": 32, "name": "xyz man", "dob":"01/01/1990"}
d2 = {"age": 45, "adress": 326777, "gender": "M"}

# Update with Another Dictionary
d.update(d2)
print(d)

# Update with Iterable
# d1.update([(k1, v1), (k2, v2)])
d.update([("dob", "20/07/2000"), ("age", 78)])
print(d)

# Update with Keyword Arguments
d.update(age=99)
print(d)

# The clear() method in dict class removes all the elements from the dictionary object and returns an empty object.
d2.clear()
print(d2)

# Union of two dictionary objects, retuning new object
print(d | d2)

