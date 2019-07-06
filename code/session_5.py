# Convert a string to a list excluding the spaces
# list(string)  # does not remove spaces
r = []
for char in string:
   r.append(char)

print(r)
# ['w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']

# Write a list comprehension to filter space and print each char 3 times
r = [ 3 * char for char in string if char != ' ']


list_of_str = ['This', 'is', 'A', 'List', 'OF', 'STrings', 1000, 3.14]

# lower_str_list = [ element.lower() for element in list_of_str]
# error: AttributeError: 'int' object has no attribute 'lower'

lower_str_list = [element.lower() for element in list_of_str if type(element) == str]

# Print items separated by ","
for item in lower_str_list:
    print(item, end=',')

# List to string
# Syntax: str.join(list) - > string
list_as_str = ','.join(lower_str_list)
print(list_as_str)


# Task: Create a list from a tuple ('a', 3.14, 'volume', 54, 'sphere', 22/7)
# that should have all numbers multiplied by 5

tuple_element=('a', 3.14, 'volume', 54, 'sphere', 22/7)
# number_mul_of_5=[5 * element for element in tuple_element if type(element)!=str]


number_mul_of_5 = [
    5 * element
    for element in tuple_element
    if type(element) in (int, float)
]

# Usual way of creating a list
number_mul_of_5 = []            # define
for element in tuple_element:
    if type(element) in (int, float):
        number_mul_of_5.append(element)


# d = {str(i): i for i in [1,2,3,4,5]}   # dict of num: num
print(number_mul_of_5)

# Task: Create a dictionary using comprehension
# input_list: [1,2,3,4,5]
# key: string representation of list item. Example: '1', '2'
# value: a tuple of the number itself and it's type. Example: (1, <class 'int'>)
d = {str(i): (i, type(i)) for i in [1,2,3,4,5]}
print(d)


"""
    list.count(item) returns the number of times the
    item exists in the list
"""
print(list.count)
# <method 'count' of 'list' objects>

"""
Command line:

l = [1,2,3,1,2,3,1]
l.count(1)
3


l.count(3)
2

l.count(0)
0
"""

"""
    Task: Given a list, cmd_history, which contains the commands issued in a
          linux server. Create a dictionary comprehension that uses the below
          list with command as key and value as the number of times the command
          is present in the list
"""

# Usual way
cmd_history = [
    'ps -ef',
    'subprocess',
    'fork',
    'fork',
    'mkdir',
    'ps -ef'
]  # input list

cmd_count = {}  # result dictionary

for cmd in cmd_history:
    cmd_count[cmd] = cmd_history.count(cmd)   # create key with cmd and value with count


print(cmd_count)

# List comprehension way
cmd_count = { cmd: cmd_history.count(cmd) for cmd in cmd_history }
print(cmd_count)

"""
    Write a dictionary comprehension which prints the words containing 'a' or 'u' in them as keys
    and value as number of characters in that wordself. Hint: str.split()

    example:
        input string: update, awk
        result dictionary: {'update': 6, 'awk': 3}
"""

text = """Contents:
  1. if - else
     if - elif - else (nested if else)
  2. for loop
  3. Iterables
      A. String traversal
      B. List
      C. Tuple
  4. Dictionary
    - Create, item existence
    - Create from list or tuple
    - Update, Delete, Sort andtraversal
    - Commonly used dictionary methods"""

sample_dict= {string: len(string) for string in text.split() if 'a' in string or 'u' in string}

print(sample_dict)
