1. How to convert a list into a tuple? Give example.

>>> my_list = [1,2,3,4,5]
>>> my_tuple = tuple(my_list)
>>>
>>> my_tuple
    

2. How to convert a string into a list? Give example.
>>> my_string = 'hello world'
>>> my_tuple = tuple(my_string)
>>> print(my_tuple)
('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')


3. What is the difference between list's append() method and extend() method. Give example with a simple list.
>>>
>>> my_list.append('6') # only one element can be added at end
>>> print(my_list)
>>> [1, 2, 3, 4, 5, 6]
>>> 
>>> my_list.extend(my_list) # entire list can be appended to the end
>>> print(my_list)
[1, 2, 3, 4, 5, '6', 1, 2, 3, 4, 5, '6']
>>>


4. Using "range" function, create a list of numbers with variable name "hundreds" which holds numbers like [100, 200, 300 ... 1000]
(To print this variable you need to type-cast the variable with list() function)
>>>
>>> hundreds = range(100, 1001, 100)
>>>
>>> list(hundreds)
[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
>>>

5. Create a list "alpha_list" using square brackets which holds alphabets 'b, c and d' as elements.

    1. After creating the list, Use a list method to insert the letter 'a' at the first 
    2. Change the last element into capital [a, b, c, D]. Use last element's index inside square brackets to reassign.
    3. Use list slicing, reverse this list and print. [D, c, b, a]    
    4. Print the size of the list
    5. lowercase the first element 

>>> alpha_list = ['b', 'c', 'd']
>>>
>>> # 1. insert a at first

>>> alpha_list.insert(0, 'a')
>>> alpha_list
['a', 'b', 'c', 'd']
>>>
>>> alpha_list[-1] = alpha_list[-1].capitalize()
>>> alpha_list
['a', 'b', 'c', 'D']
>>>
>>> alpha_list = alpha_list[::-1]
>>>
>>> print(alpha_list)
['D', 'c', 'b', 'a']
>>>
>>> alpha_list[0] = alpha_list[0].lower()
>>>
>>> alpha_list
['d', 'c', 'b', 'a']


6. Sort the list in-place. The list must now look like: [D, a, b, c] 
>>> alpha_list.sort()
>>>
>>> alpha_list
['a', 'b', 'c', 'd']


7. Use list slicing to remove the last element in the list "alpha_list". The list must look like [a, b, c]
   Hint: list[:-1].
   
   
>>> alpha_list = alpha_list[:-1]
>>>
>>> alpha_list
['a', 'b', 'c']
    
   
8. Now add the letters d, e, f, g, h towards the end of the list alpha_list

>>>
>>> alpha_list.extend(['d', 'e', 'f', 'g'])
>>>
>>> alpha_list
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>

9. Use for loop to loop through numbers from 0 to 100 and print its cubes only if the cubed value is divisible by 5 in the same line separated by single space
   
   Hint: a number is divisible by 5 means, number % 5 == 0
    
>>> for num in range(0, 101):
...   if num **3 % 5 == 0:
...     print(num ** 3)
...
   
10. Given two lists, find the common numbers in both the lists.
    
l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
    
    1. convert these lists to two sets, s1 and s2 (type-cast with set() function)
    2. print all the numbers that are common in both the sets. Hint. set1.intersection(set2)

>>> l1 = [1,2,3,4,5]
>>> l2 = [4,5,6,7,8]
>>>
>>> s1 = set(l1)
>>> s2 = set(l2)
>>> s1
{1, 2, 3, 4, 5}
>>> s2
{8, 4, 5, 6, 7}
>>> s1.intersection(s2)
{4, 5}
    
11. Create a set with values a, b, c, d and e. Try to add 'a' and 'e' to the list again.

    is the set ordered in the way they are created?
    What happens returned while adding duplicate element to this set?
    How would you avoid error while removing an inexistent element from a set? What was the error?
    
    
>>> myset= {'a', 'b', 'c', 'd', 'e'}
>>> myset.add('a')
>>> myset.add('e')
>>> myset
{'d', 'e', 'c', 'a', 'b'}
>>> # no changes while adding
...
>>>
>>> myset.remove('d')               # removes element if exist 
>>> myset
{'e', 'c', 'a', 'b'}
>>> myset.remove('z')               # KeyError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'z'
>>>
>>> myset.discard('z')    # Silently ignores inexistent element 
    
12. Create:

    1. An empty dictionary and print its type.
    2. Create a dictionary with keys and values: a=alphabet, 1=number, 3.14=float. Hint: variable = {key1: value1, key2: value2, ...}
    3. Given a list of tuples: [(1, 1), (2, 4), (3, 9)]. Convert this into dictionary and name it with variable square_dict 

>>> # Method 1:
>>> random_dict = {'a': 'alphabet', 1: 'number', 3.14: 'float'}
>>> # Method 2:
>>> random_dict = {}
>>> random_dict['a'] = 'alphabet' # inexistent key, so key-value pair is added to dict
>>> random_dict[1] = 'number'
>>> random_dict[3.14] = 'float'
>>>
>>> print(random_dict)
{1: 'number', 3.14: 'float', 'a': 'alphabet'}
>>>
>>> # Method 3:
>>> kv_pairs = [  ('a', 'alphabet'), (1, 'number'), (3.14, 'float')  ]   # list of tuples
>>> random_dict = dict(kv_pairs)
>>>
>>> print(random_dict)
{1: 'number', 3.14: 'float', 'a': 'alphabet'}
>>>
    

13. Using square brackets approach modify square_dict as follows:
    1. Add a key 4 and its square as value 
    2. Try to print the square of the number 5. What is the error returned?
    3. How do you suppress this error when accessing an inexistent key, 5? Try to return message, 'Undefined' for all the keys that do not exist in the dictionary
    
>>> square_dict = {1: 1*1, 2: 2*2, 3:3*3}
>>> print(square_dict)
{1: 1, 2: 4, 3: 9}
>>> #square bracket apprach
...
>>> square_dict[4] = 4 * 4
>>> print(square_dict)
{1: 1, 2: 4, 3: 9, 4: 16}
>>> # update method approach
...
>>> square_dict.update( {4: 4*4} ) # update method updates a dictionary as a whole
>>> print(square_dict)
{1: 1, 2: 4, 3: 9, 4: 16}
>>>
>>> square_dict[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 5
>>>
>>> # suppress KeyError and return Undefined message
... square_dict.get(5, 'undefined')
'undefined'
>>>
>>>
>>> square_dict.get(10, 'ten is not allowed :P')
'ten is not allowed :P'
>>>


14. Use dictionary methods to print the following in square_dict:
    1. all the keys 
    2. all the values
    3. all the items as a list of tuple. Hint. You need to type-cast the resule of method call with list() function

    
>>>
>>> list_of_nums = square_dict.keys()
>>> list_of_keys = square_dict.keys()
>>>
>>> print(list_of_keys)
dict_keys([1, 2, 3, 4])
>>> print(list(list_of_keys)) # Type-cast to list
[1, 2, 3, 4]
>>> list_of_values = square_dict.values()
>>> print(list(list_of_values)) # Type-cast to list
[1, 4, 9, 16]
>>> list_of_items = square_dict.items()
>>>
>>> print(list(list_of_items)) # Type-cast to list
[(1, 1), (2, 4), (3, 9), (4, 16)]
>>>
>>>
    
    
    
15. Loop through the dictionary 'square_dict' using dict.items() and print only the keys and values for which the value is an even number. 
    Hint. An even number is, number % 2 == 0
    
    Steps:
        # Traverse using dict.items and unpack key, value inside for 
        # check if value is divisible by 2
        # if yes, print key and value 
        

>>> # Method 1: Traversing the dictionary directly
... for num in square_dict:
...   # Square bracket approach
...   square_val = square_dict[num]
...   if square_val % 2 == 0:    # Modulo 2 if equals to 0, then its even no.
...     print(square_val)
...
4
16
>>>
>>> # Method 2: Traversing using dictionary's item method
... for num, square_val in square_dict.items():
...   if square_val % 2 == 0:
...     print(square_val)
...
4
16
>>>
>>>
        
16. Create an employee database that looks like below. Here the employee's id is key and his details is value (which is a list).

    emp_db = {
        100: {
            'name': 'emp_100', 
            'dept': 'sales',
            'exp': 10,
        },
        200: {
            'name': 'emp_200', 
            'dept': 'sales',
            'exp': 8,
        },
        300: {
            'name': 'emp_300', 
            'dept': 'sales',
            'exp': 11,
        },
        400: {
            'name': 'emp_100', 
            'dept': 'sales',
            'exp': 12,
        },
    }
    
    From the above database, print the name, dept and exp of all employees whose experience is greater than 10 years.
    
    Algorithm:
    
        Step 1: Traverse through each dictionary as it is without using .items() [for emp_id, emp_details in emp_db.items()]
        Step 2: Here emp_details is again a dictionary. From this dictionary, fetch the exp and store in a variable
        Step 3: Check if the exp > 10
        Step 4: If yes, now fetch the other details such as the name, dept from this exp_details dictionary
        Step 5:     print details 
    
>>> for emp_id, emp_details_dict in emp_db.items():     # loop using items method 
...     exp = emp_details_dict.get('exp')               # each value in the nested-dictionary is in turn a dict
...     if exp > 10:                                    # comparison
...         name = emp_details_dict['name'] # square bracket approach   # fetch name and dept
...         dept = emp_details_dict['dept']
...         print('name={}, exp={}, dept={}'.format(name, exp, dept))   # print using format string 
...

name=emp_300, exp=11, dept=sales
name=emp_100, exp=12, dept=sales
name=emp_100, exp=10, dept=sales


17. Create a dictionary 'schools_dict' which has 
        - the key 'class_a' and value with a list of students varun, arun, tarun.
        - the key 'class_b' and value with a tuple of students vani, rani and shalini
        
    
    Question and Steps:
    
        - Create an empty list "students_list"
        - then traverse through the dictionary in any method of your choice and build the list with students names alone (Hint: you can use extend method)
        - Finally print the students names
        It should be like [varun, arun, tarun, vani, rani, shalini]
        
>>> for key, names_list in schools_dict.items():    # loop using items method 
...   students_list.extend(names_list)              # extend the dictionary directly
...
>>> print(students_list)
['vani', 'rani', 'shalini', 'varun', 'arun', 'tarun']
