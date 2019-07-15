# I. Use list comprehension for below 3 questions.
#    Name the functions yourself. It should be related to the type of functioning it does

    # 1. Write a function which gets two arguments (min, max) returns even numbers between min and max.

def get_even_numbers(min, max):
    return [number for number in range(min, max + 1) if number % 2 == 0]

    # 2. Write a function which gets a list as argument and returns all words as list whose length
    #    is greater than 5 and starts with 'a' or 'b'
    #
    #    sample input :
    #    input_list = ['amazing', 'excel', 'affluent', 'rest', 'benign', 'best', 'bounty', 'token', 'assault']
def get_words(src_list):
    return [word for word in src_list if len(word) > 5 and word[0] in ('a', 'b') ]

    # 3. Write a function that accepts two arguments (reference_words, input_words). It should return a list
    #    that checks input_words against reference_words and returns only the words that not matching both lists.

ref_words = ['comprehension', 'list', 'generators', 'functions', 'tuple']
input_words = ['list', 'tuple', 'string']

def get_matching_list(reference_words, src_list):
    return [word for word in input_words if word in reference_words]

# II. Use dictionary comprehension for below 3 questions.
#     Please name the functions yourself. It should be related to the type of functioning it does
#
#     4. Write a function that takes an argument max_number and it should return a dictionary in below format.
#
#        For instance, max_number = 5. Then the resulting dictionary should be { '1': 1, '2': 2, '3': 3, '4': 4, '5': 5 }
#        Key as string form of that number and value in integer format
#
#        Hint: str(1) = '1'
def get_dict(max_number):
    return { str(number): number for number in range(max_number + 1)}

#     5. Write a function that takes a list argument and returns a dictionary with keys as elements in the input list
#        and values as the number of characters in each word. Ignore if an element is not string
#
#        sample input:
#         fruits = ['apple', 1, 'mango', 2, 'banana', 3, 'cherry']
#
#        sample output:
#         {'apple': 5, 'mango': 5, 'banana': 6, 'cherry': 6}
def word_length_dict(in_list):
    return {word: len(word) for word in in_list if type(word) is str}
#
#     6. Write a function that takes a list argument and returns a dictionary with keys in the input list
#        in all lowercase and values in all uppercase. Ignore if an element is not string/
#
#        sample input:
#         fruits = ['apple', 1, 'mango', 2, 'banana', 3, 'cherry']
#
#        sample output:
#         {'apple': 'APPLE', 'mango': 'MANGO', 'banana': 'BANANA', 'cherry': 'CHERRY'}
#
fruits = ['apple', 1, 'mango', 2, 'banana', 3, 'cherry']
def word_upper_dict(in_list):
    return {word.lower(): word.upper() for word in in_list if type(word) is str}

# III. Use set comprehension for below 1 question
#      Please name the functions yourself. It should be related to the type of functioning it does
#
#     7. Write a function that takes a list of numbers with duplicate values. The function should return a set with squares of each
#        number only if the number is an integer and ignore all other types (str, float, etc.)
#
#        Sample input:
#           input_list = [1, '1', 'a', '1', 2, '2', 'c', 'd', 3, '3', '4', '4', 4, 5]
#
#        Sample output:
#           {16, 1, 9, 25, 4}
input_list = [1, '1', 'a', '1', 2, '2', 'c', 'd', 3, '3', '4', '4', 4, 5]
def get_set_from_list(in_list):
    return {item for item in in_list if type(item) is int}

# IV. Write lambda function for the below 3 questions
#
#     8. Write a lambda function with no arguments. When called it should print message: "i'm function or anonymous function"

f = lambda : print("i'm function or anonymous function")
f()

#     9. Write a lambda function with one argument "n" it should return the square root of the given number
sq_root = lambda x: x ** 0.5
sq_root(9)

    # 10. Write a lambda function with one argument. It should return 3rd item in the given sequence

third_item_getter = lambda x: x[2]
print(third_item_getter('PyThon'))

# V. Sorting dictionary by value:
# 
#     11. Write a function "get_sorted_school_strength" that takes one argument which is a dictionary of school name and its strength (sample data below).
#         The function should:
# 
#           a. raise ValueError, if the argument passed to the function is not of type 'dict'
#           b. define a lambda function to return second element in the sequence
#           c. use sorted() function to sort the dictionary by values in ascending order
# 
#           sample_input:
#             school_db = {'school_a': 500, 'school_b': 300, 'school_c': 700, 'school_d': 250}
# 
#           sample output:
#             [('school_d', 250), ('school_b', 300), ('school_a', 500), ('school_c', 700)]

school_db = {'school_a': 500, 'school_b': 300, 'school_c': 700, 'school_d': 250}
second_item = lambda x: x[1]
sorted_list = sorted(school_db.items(), key=second_item)
for key, value in sorted_list:
    print(key, value)
# school_d 250
# school_b 300
# school_a 500
# school_c 700

    # 12. Write a function "get_country_population" that takes one argument which is a dictionary of country name and its population (sample data below).
    #     The function should:
    # 
    #       a. raise ValueError, if the argument passed to the function is not of type 'dict'
    #       b. define a lambda function to return second element in the sequence
    #       c. use sorted() function to sort the dictionary by values in DESCENDING  order
    # 
    #       sample_input:
    #         population_db = {'India': 12000000, 'New Zealand': 400000, 'China': 180000000, 'America': 800000}
    # 
    #       sample output:
    #         [('China', 180000000), ('India', 12000000), ('America', 800000), ('New Zealand', 400000)]

def get_country_population(input_dict):
    if type(input_dict) != dict:
        raise ValueError('Required value for input_dict should of dict type!')
    second_item = lambda x: x[1]
    return sorted(input_dict.items(), key=second_item, reverse=True)


get_country_population(population_db)
# [('China', 180000000), ('India', 12000000), ('America', 800000), ('New Zealand', 400000)]


# VI. Generator Functions
# 
#     13. Given the below generator function, use next() function to traverse through the generator one by one and observe the
#         error thrown at after the generator is exhausted

def square_generator(max_limit=5, start=0):
    for number in range(start, max_limit + 1):
        yield number ** 2

gen_obj = square_generator(4)
next(gen_obj)   # 0
next(gen_obj)   # 1
next(gen_obj)   # 4
next(gen_obj)   # 9
next(gen_obj)   # 16
next(gen_obj)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

#     14. Conceptual questions:
#           1. What is the use of next() function
                It is used to fetch and return the next item in the generator or iterator 
#           2. What is the error thrown when generator is exhausted?
                StopIteration
#           3. How are generators memory efficient?
                Generators return only one value at a time, hence at any point in time 
                only one item gets stored in the memory when compared to list or other 
                data types which stores many items in memory
#           4. What is the difference between yield and return keyword?
                yield:
                    1. is used to created generator functions 
                    2. it returns the value to the caller, say a for loop and 
                       also remembers the state of the function 
                return:
                    1. is used to return a value and terminate the function call 
                    2. it does not store the state of the function 
#           5. Do we require StopIteration error to be raised explicitly in generators?
                No. A generator function automatically raises StopIteration when the 
                generator gets exhausted. raise StopIteration statement is not Required
                to  be mentioned explicitly


    # 15. Given a list of file paths below as a single string. Write a generator function with no arguments
    #     to return python file paths one at a time.
    # 
    #     Hint: paths to python file ends with ".py". str.endswith(text) returns True when matches

        paths = """corelib/VM_manage/manage_config.yaml
            corelib/core/api_util.py
            corelib/logger/system_log.log
            corelib/python_packages_install/
            corelib/schema/plan.py
            corelib/selenium/core/api.py
            corelib/service_handler/requirements.txt
            corelib/snapshots/snaphsot_getter.py
            corelib/subzero/loader.py
            tests/core/testfile.txt
            tests/configurations/core/wlc.py
            tests/configurations/ise/core/config_reader.py
            tests/configurations/ise/ui/core/framework.py
            tests/configurations/ise/ui/administration/core/empty_container.py
            tests/configurations/ise/ui/administration/system/core/core_fw.py
            tests/configurations/ise/ui/administration/system/logging/core/
            tests/suites/core/suite_configurator.py
            tests/suites/system_test/core/
            tests/suites/system_test/dataholder/core/dataholder.py
            tests/suites/system_test/systestconfiguration/core/
            tests/suites/system_test/systestvalidation/core/validate.py"""

def python_file_generator(path_list):
    for path in path_list.split('\n'):
        if path.endswith('.py'):
            yield path

for file in python_file_generator(paths):
    print(file)


""""
corelib/core/api_util.py
corelib/schema/plan.py
corelib/selenium/core/api.py
corelib/snapshots/snaphsot_getter.py
corelib/subzero/loader.py
tests/configurations/core/wlc.py
tests/configurations/ise/core/config_reader.py
tests/configurations/ise/ui/core/framework.py
tests/configurations/ise/ui/administration/core/empty_container.py
tests/configurations/ise/ui/administration/system/core/core_fw.py
tests/suites/core/suite_configurator.py
tests/suites/system_test/dataholder/core/dataholder.py
tests/suites/system_test/systestvalidation/core/validate.py
"""
