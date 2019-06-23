""" if blon"""
if True:
    print('Hello')
    print('World!')
    print('Hello')
    print('Hello')

"""
    Operators in Python

    universal
        ==      - equal to
        !=      - not equal to
        is      - equals
        in      - check if item exists in iterable
        not in  - check if item does not exists in iterable

    numbers and floats
        <  - Less than
        >  - Greater than
        <= - Less than or equal to
        >= - Greater than on equal to
"""


""" if else, if - elif - else """
name = 'rajesh' # assignment

if name != 'rajesh':
    print('read and write access')
else:
    print('access denied')


"""
    Nested if else statement

    if - elif - else
"""

if 1 > 2:
    print('one is gt than 2')
elif 2 > 3:
    print('two is greater than 3')
elif type('vivek') != str:
    print('"Vivek" is a string')
else:
    print('no matches')
# end of statement

# for loop with a list
for n in [1, 2, 3, 4]:
    print(n, end=' ')
print() # Print and new line

# for in str
for n in 'hello world':
    print(n, end=',')
print()

""" for - break - else """
name_list = ['arjun', 'murugan', 'rajesh', 'vivek']
# is_present = False

for name in name_list:
    if name == 'vivek':
        # is_present = True
        print('present')
        break
else:
    print('vivek is absent')

# if is_present != True: # not False == True
#     print('vivek is absent')


# 3.B.2 Search a list (or any iterable - set, dict, string, tuple):
# - Searching a list is done using 'in' keyword

if 'VIVEK' in name_list :
    print('present')
else:
    print('vivek is absent')

"""
    List Slicing
"""

# 1. How to reverse a list?
print(name_list)
print('Reversed list (list slicing):')
print(name_list[::-1])
print(name_list)
print()

name_list = ['arjun', 'murugan', 'rajesh', 'vivek', 'swadhi']

print('Reversed list (reverse method):')
reversed_names = name_list.reverse()
print(name_list)
print(reversed_names) # None
print()

 # Slicing in steps of 2 or 3
values = name_list[::3]
print(values)

# del keyword
print(name_list)

print('first element:', name_list[0])
del name_list[0]

print('first element:', name_list[-1])
del name_list[-1]
print(name_list)

del name_list   # del <object>
print(name_list)

# Remove first two elements in the below list
print(name_list)
name_list = name_list[2:]
print(name_list)

# Delete the entire list
del name_list = []
print(name_list)
print()
print()

cubes = [1**3, 2**3, 3**3]
print(cubes)

# for number in [4, 5, 6]:
#     cubes.append(number ** 3)

cubes.extend( [4**3, 5**3, 6**3] )

print(cubes)


 SIngle valued tuples
t = (1)
# 1
print(t)
print(type(t))
#<type 'int'>
t = (1,)
print(type(t))
#<type 'tuple'>
print(t)
#(1,)

# Is it possible to modify the list inside the tuple?
t = ([1,2,3], 'a', 'b')
print(t)
l = t[0]

l.append(4)
print(l)

# Build a tuple from a string
s = 'welcome to coding'
print(len(s))
t_from_s = tuple(s)
print(t_from_s)
print(len(t_from_s))
print('No. of spaces in tuple:', t_from_s.count(' '))
print('first index of space:', t_from_s.index(' '))
