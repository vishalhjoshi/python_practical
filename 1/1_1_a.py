my_dict = {}  # empty dictionary

my_dict = {1: 'apple', 2: 'ball'}  # dictionary with integer keys
print(my_dict)


my_dict = dict({1:'apple', 2:'ball'})  # using dict()
print(my_dict)

my_dict = dict([(1,'apple'), (2,'ball')]) # from sequence having each item as a pair
print(my_dict)

my_dict = {'name': 'Vishal', 'age': 23}  # dictionary with mixed keys
print(my_dict)

print(my_dict['name'])

print(my_dict.get('age'))

# update value
my_dict['age'] = 24

print(my_dict)

# add item
my_dict['address'] = 'Jamner'

print(my_dict)


# remove a particular item
print(my_dict.pop('address'))

print(my_dict)

#  remove an arbitrary item

print(my_dict.popitem())

print(my_dict)

#  delete a particular item
del my_dict['name']

print(my_dict)

# remove all items
my_dict.clear()

print(my_dict)

# delete the dictionary itself
del my_dict

#Throws Error
#print(my_dict)