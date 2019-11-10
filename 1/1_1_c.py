# Python code to demonstrate Adding Key Value Pairs
# finding duplicate values from a dictionary

stud_dict = {
    'name':'vishal',
    'age':23,
}

print("Student :", str(stud_dict))



stud_dict['address'] = 'Jamner' #adding Key Value Pair

stud_dict['Age'] = 23



rev_dict = {}

for key, value in stud_dict.items():
    rev_dict.setdefault(value, set()).add(key)

result = [key for key, values in rev_dict.items()
          if len(values) > 1]

# printing result
print("duplicate values", str(result))
