empty_dict = {}
print(empty_dict)
print(type(empty_dict))

empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

"""
2. How to find if an item exists in a dictionary?
- in keyword
"""

fruit_dict = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cherry'
}

if 'd' in fruit_dict:
    print('d is found')
else:
    print('d is NOT found')

# standard way of creation
student_dict = {
    'name': 'Suresh',
    'grade': 'B',
    'id': 100
}

# Tuple of 3 tuples
# Tuple of 3 les
student_tuple = (
    ('name', 'Suresh'), ('grade', 'B'), ('id', 100)
)
student_dict = dict(student_tuple)
print(student_dict)

# List of 3 lists
student_tuple = [
    ['name', 'Suresh'], ['grade', 'B'], ['id', 100]
]

student_dict = dict(student_tuple)
print(student_dict)

# More than 2 element in a list will throw
# ValueError: dictionary update sequence element #0 has length 3; 2 is required

# Dictionary access
# 1. Common way - Square brackets
emp_dict = {'name': 'swad', 'language': 'python', 'org': 'hcl'}
print(emp_dict['language'])
## print(emp_dict['age'])  # KeyError

print(emp_dict.get('age', 'undef'))
print(emp_dict.get('next', 'tcs'))
print(emp_dict.get('name', 'Not Defined'))


# Update an item
emp_name = emp_dict['name']
print('before changing', emp_name)

# updating an already existing key
emp_dict['name'] = 'rajesh'
emp_name = emp_dict['name']
print('after changing', emp_name)

# updating an inexistent key -> add the key
emp_dict['year'] = 2017
emp_dict['age'] = 29
print(emp_dict)

# delete a dictionary
print('deleting emp dictionary ...')
del emp_dict
## print(emp_dict)   # NameError after deleting


# delete a specific key-value pair (item)
del emp_dict['language']
print(emp_dict)

# sorting a dictionary
emp_dict[10] = 'number ten'
emp_dict[1] = 'number one'
print(emp_dict)
sorted_keys = sorted(emp_dict)
print(sorted_keys)

# dict of numbers
num_dict = {
    10: 'ten',
    0: 'zero',
    5: 'five'
}
print(num_dict)
sorted_keys = sorted(num_dict)
print(sorted_keys)


"""
    Common methods in dictionary

    - dict.keys()
    - dict.values()
    - dict.items()
    - dict.get()
    - dict.update()
    - dict.clear()
    - dict.pop()
    - dict.popitem()
"""

emp_keys = emp_dict.keys()
print('Keys in dictionary:')
for emp_key in emp_keys:
    print('  ', emp_key)

emp_keys = list(emp_keys) # Type casting for the sake of printing
print('emp dictionary keys:', emp_keys)

emp_values = emp_dict.values()
print()
print('Values in dictionary:')
for emp_val in emp_values:
    print('  ', emp_val)

emp_items = emp_dict.items()
print()
print(list(emp_items))
print()
print('Items in dictionary:')
for emp_item in emp_items:
    print('  ', emp_item, ':', type(emp_item))

"""
emp_dict['exp'] = 8
emp_dict['city'] = 'chennai'
emp_dict['shift'] = 'day'
"""
updated_values = {
    'exp': 8,
    'city': 'chennai',
    'shift': 'day'
}
emp_dict.update(updated_values)
print(emp_dict)

emp_dict.clear()
print(emp_dict)

print(updated_values)

# dict.pop(key) method
emp_exp = updated_values.pop('exp')
print('experience:', emp_exp)

# dict.popitem()
popped_item = updated_values.popitem()
print('Popped item:', popped_item)
popped_item = updated_values.popitem()
print(updated_values)
print('Popped item:', popped_item)

# traverse a Dictionary
print(updated_values)

for key in updated_values: # No methods used  = dict.keys()
    print(key, updated_values[key])

for key, value in updated_values.items(): # No methods used  = dict.keys()
    print(key, value)

student_db = {}

student_1 = {'name': 'arjun', 'age': 25, 'grade': 'A'}
student_2 = {'name': 'rajesh', 'age': 27, 'grade': 'B'}
student_3 = {'name': 'vivek', 'age': 29, 'grade': 'C'}

from json import dumps

# dict of dict
student_db = {
    'student_1': student_1,
    'student_2': student_2,
    'student_3': student_3
}


print('Student database:')
print(dumps(student_db, indent=2))

school_db = {
    'students': [student_1, student_2, student_3],   # list of dictionaries
    'teachers': ['teacher1', 'teacher2', 'teacher3']
}

print('School database:')
print(dumps(school_db, indent=2))
print()

# traverse each student in school_db
for student in school_db.get('students'):   # [{}, {}, {}] list of student dicts
    # Here, student is a dictionary
    name = student.get('name')
    # Check if the student's name is rajesh
    if name == 'vivek':
        # Print the student details
        # print(name, ',', student.get('age'), ',', student.get('grade'))
        print(name, ',', student['age'], ',', student['grade'])
