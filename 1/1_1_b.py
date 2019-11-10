# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art' # Immutable

print(tuple_1)
print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()


# declaring list with integer elements
list1 = [10, 20, 30, 40, 50]

# printing list1
print("List 1 Elements are ",list_1)


# printing elements of list1 by index
print("Printing Tuple Elements @ 0 Index : ",tuple_1[0])
print("Printing Tuple Elements @ 1 Index : ",tuple_1[1])
print("Printing Tuple Elements @ 2 Index : ",tuple_1[2])
print()  #prints Empty line

# printing elements of list1 by index
print("Printing list Elements @ 0 Index : ",list_1[0])
print("Printing list Elements @ 1 Index : ",list_1[1])
print("Printing list Elements @ 2 Index : ",list_1[2])
print("Printing list Elements @ 3 Index : ",list_1[3])
print()  #prints Empty line


string  = "Python"
print(string) #printing string
print("Printing  String @ 0 Index : ",string[0])
print("Printing  String @ 1 Index : ",string[1])
print("Printing  String @ 2 Index : ",string[2])
print("Printing  String @ 3 Index : ",string[3])
print("Printing  String @ 4 Index : ",string[4])
print("Printing  String @ 5 Index : ",string[5])