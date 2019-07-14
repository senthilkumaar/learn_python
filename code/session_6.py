# Callback functions
def add(n1, n2):
    return n1 + n2

add(1, 2)

def mul(n1, n2):
    return n1 * n2

def sorted(num1, num2, function):
    result = function(num1, num2)     # third arg function is called with first two args
    print(result)

def first_item(sequence):
    return sequence[0]

def second_item(sequence):
    return sequence[1]

d = {'messages': 1, 'requests': 2, 'notifs': 3}

def print_dict_item(dictionary, func=first_item):
    """ Prints the keys of each dictionary key-value pair"""
    dict_items = dictionary.items()    # key-value pair as List of tuples form
    for key_value_tuple in dict_items: #[(), ()] - > ()
        key = func(key_value_tuple)
        print(key)


print_dict_item(d, func=first_item)
print_dict_item(d, func=second_item)


# Lambda functions

# Lambda function to find the first element in a sequence
first_item = lambda x: x[1]

add_ten = lambda a : a + 10   # one argument
print(add_ten(5))

# Lambda function that generates mail id from first, last and company name
mail_id = lambda f_name, l_name, c_name: '{}.{}@{}.com'.format(f_name, l_name, c_name)
print(mail_id('john', 'doe', 'company'))

# Simple examples
average = lambda l: sum(l) / len(l) # calculate average of numbers in a list
average([10, 10, 10, 10])

# Sort dictionary by value
people_count_dict = {
  'hcl': 1000,
  'tcs': 1200,
  'cts': 650,
  'wipro': 700
}

# Normal sorting
sorted(people_count_dict)   # sorts company names in alphabetical order

# To sort by values
# 1. Use sorted() function on dict.items() -> list of tuples [(a, b), (c, d), ...]
# 2. Pass the keyword argument 'key' with the lambda function.
lambda x: x[1]

sorted(people_count_dict.items(), key=lambda x: x[1])
sorted(people_count_dict.items(), key=lambda x: x[1], reverse=True)

# generators
ez_string = "Generators     of numbers".split()
for s in ez_string:
    print(s)

# Example 1:
def alpha_generator():
    yield 'a'
    yield 'b'
    yield 'c'


alpha = alpha_generator() # invoke using next function
next(alpha) # 'a'
next(alpha) # 'b'
next(alpha) # 'c'
next(alpha)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# 2. Example without loops
def gen_printer():
    n = 1
    print('This is printed first')
    yield n   # returns the value and the state is stored
    n += 1
    print('This is printed second')
    yield n   # returns the value and the state is stored
    n += 1
    print('This is printed at last')
    yield n   # returns the value and the state is stored


printer = gen_printer()
next(printer)
# This is printed first
# 1
next(printer)
# This is printed second
# 2
next(printer)
# This is printed at last
# 3
next(printer)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


# Create a generator that returns square of given numbers
def square_generator(max_limit, start=0):
    for number in range(start, max_limit + 1):
        yield number ** 2

sq = square_generator(10)
for s in sq: # for s in square_generator(10)
    print(s)


# create a generator function that returns line by line from a large noisy data

def generate_lines():
    text = """ACP Milind Khetle said Sam called his wife in Sydney, Australia, and
----------
told  her he was going to end his life. His wife immediately informed the British
==========
deputy high commission in Mumbai. Officials from the foreign mission informed the police control room
19999999999991232
A team led by ACP Khetle immediately swung into action and reached the address in Hiranandani Gardens
**************
around 10 am"""
    for line in text.split('\n'):   # Traverse through each line
        if '-' in line or    \
           '==' in line or   \
           line.isdigit() or \
           '*' in line:
            continue
        yield line

for line in generate_lines():
    print(line)


# Practise questions
input_list = input_list = range(1, 51, 3)

# list(input_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 1. Construct a list of even numbers
# print(list(input_list))

# even1_list = [item for item in input_list if item % 2 == 0]
# print(even1_list)
#
# odd1_list = [item for item in input_list if item % 2]
# print(odd1_list)
#
# index_list = [
#     item
#     for item in input_list
#     if input_list.index(item) % 2 == 0
# ]
#
# print(index_list)

#
# 1. Write a lambda function that takes a list argument and returns each item in the lists
# multiplied by 3
input_list = [1, '1', 'a', '3', 4]
# output_list = [3, '111', 'aaa', '333', 12]


# 2. Write a lambda function that takes two arguments /
# i. number
# ii. power
#
# func(4, 2) -> 16
# func(2, 3) -> 8

l = [1, '1', 'a', '3', 4]
mul_3 = lambda l: l*3
print(mul_3)

pow = lambda x, y: x ** y
print(pow(3, 4))

temp_list_comp = [item * 3 for item in input_list]
print(temp_list_comp)
thrice = lambda input_list: [item * 3 for item in input_list]

"""
Write a generator function "get_square_generator" that takes an argument max_limit
it should return squares of any number when it is

1. divisible by 2 or
2. divisible by 5
"""
def get_square_generator(max_lim):
    for num in range(1, max_lim + 1):
        if num % 2 == 0 or num % 5 == 0:
            yield num ** 2

for i in get_square_generator(max_lim=10):
    print (i)
