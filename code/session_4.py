def square(n):
    return n ** 2


def power(x, y):
    return x ** y

n = 5
# n_sq = square(5)
print(square(5))
print(square(10))
print(square(11))
print(square(12))


def send_email(to_list, cc_list, mail_sub, mail_content):
    # process to_list
    # process cc_list to html
    # mail_sub to html
    # assemble and trigger email
    pass

"""
    Usual way of calling:
        rv = send_email([], [], 'test sub', 'sample mail content')


        Error when insufficient args:
        TypeError: send_email() takes exactly 4 arguments (3 given)

    Another way to call:

    >>> send_email(mail_content='test content', cc_list=[], to_list=[], mail_sub='sample')
    'success'

    (Ordering is not required while calling as keyword arguments)

Real time example:
    # production run
    # send_mail()

    # nightly job
    # send_mail()

    # if success
        # send_mail([directors, managers, developer])
    # if fail
        # send_mail('developers')

    Code Reusablity:
        So many calls to the same function reduces the code being rewritten
"""

"""Default args"""

def volume_of_sphere(radius, pi=3.14):
    print('Value of pi:', pi)
    return (4/3) * pi * power(radius, 3) # 4/3 * pi * r^3

# () - means grouping in python, so tuple with single args should have 1 items
# followed by , (i, )

vol = volume_of_sphere(5)
print(vol)

vol = volume_of_sphere(pi=3.14, radius=5)   # all keyword args
print(vol)

vol = volume_of_sphere(radius=3.14, 5)
print(vol)
# SyntaxError: positional argument follows keyword argument

# 2. *args - variable number of args
def calculate_sum(*numbers):
    total = 0
    print(numbers)
    print(type(numbers))
    for number in numbers:
        total = total + number
    return total

calculate_sum()  # 0 args
result = calculate_sum(10, 20, 30)  # 0 args
print(result)

def add(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total


print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4))

def calculator(operation, *numbers):
    if operation == 'mul':
        return_val = 1
        for number in numbers:
            return_val =  return_val * number

    elif operation == 'sub':
        return_val = 0
        for number in numbers:
            return_val =  return_val - number

    return return_val


product = calculator('mul', 1, 2, 3, 4, 5)
print(product)

difference = calculator('sub', 1, 2, 3, 4, 5)
print(difference)

def person_info(**data):
    print("\nData type of argument:", type(data))
    for key, value in data.items():   # Accessing the
        print("{} is {}".format(key,value))

# Rules while calling function with kwarg
# Dont pass quotes for keys
# must pass quotes for values if it is string
person_info(firstname="John", lastname="Wood", email="johnwood@nomail.com", country="Wakanda", age=25, phone=9876543210)

# Function with all three types of args
def print_user_address(name, street_name, *area_details, **city_details):
    """
        Prints the user address details in a formatted manner

        @param    name             (string)         Name of the customer
        @param    street_name      (string)         Street address
        @param    area_details     (optional)       Additional address details
        @param    city_details     (optional)       City pin and other details
    """
    print("To,\n    {},\n    {}".format(name, street_name))

    for area_detail in area_details:
        print("    {}".format(area_detail))

    for detail_key, detail_value in city_details.items():
        print("    {}: {}".format(detail_key, detail_value))


print_user_address('Robert')   # TypeError: print_user_address() missing 1 required positional argument: 'street_name'
print_user_address('Robert', '20, john street')
print_user_address('Robert', '20, john street', '5th Main Road')
print_user_address('Robert', '20, john street', '5th Main Road', 'Landmark: (Opposite to play ground)')
print_user_address('Robert', '20, john street', '5th Main Road', 'Landmark: (Opposite to play ground)', city='Chennai', pincode=600015)

def adder(num_1, num_2):
    """
        Function name : adder
        Purpose       : Calculate sum of two numbers
        arguments     : num_1 (integer), num_2 (integer)
        return        : sum_value (integer)
    """
    return num_1 + num_2

# Raise an exception intentionally
def print_iterable(iterable):
    """
        Function that prints iterables in a formatted way

        @param  iterable    (list/tuple/dictionary)  Iterable to print
        @return None        (Exception for string args)
    """
    print('The iterable you passed is of type:', type(iterable))

    if type(iterable) is str:
        raise Exception('Strings are not allowed in this method')   # Code to raise exception

    for item in iterable:
        print('   - {}'.format(item))


# Defining a custom exception
class StringNotAllowedException(Exception):     # inherit from the class 'Exception'
    pass

# Handling the exception
l = ['192.1.1.1', '192.1.1.2', '192.1.1.3', '192.1.1.4']
s = 'Python program'
# print_iterable(s)         # Code which is subject to exception

try:
    """  Code which may fail or raise exception """
    print_iterable(s)
    print_iterable(l)
except Exception as e:
    """  Code to handle exception """
    print('****** Passing a str raised exception:', e, '******')
    # raise                                 # re-raising the same exception after logging above
    # raise TypeError('Str not allowed')    # re-raising a different meaningful exception
    raise StringNotAllowedException()       # raising a customized exception
else:
    """  Code that does not raise exception """
    print('success. other steps here ...')
    # Remaining operations
finally:
    """  Cleanup code """
    l.clear()

print_iterable(l)


# Iteration on a dictionary works over it's keys
d = {
    'Desktop-A': '192.1.1.1',
    'Desktop-B': '192.1.1.2',
    '192.1.1.3': 'Desktop-C'
}
print_iterable(d)
