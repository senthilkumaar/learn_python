"""
name = 'Saravana'
print(name)
print(type(name))

l = ["Saravana","rajesh", "Murugan", "Vivek", 1, 3, "arjun", 1.5]
print(l)
print(type(l))

t = ("Saravana","rajesh", "Murugan", "Vivek", 1, 3, "arjun", 1.5)
print(t)

print(type(t))

pi = 314
print(pi)
print(type(pi))


d = {
    # 'Swad': 29, 'Rajesh': 27, 'Arjun': 24
    'Swad': [29, 'chennai', 'hcl'],
    'Rajesh': [27, 'chennai', 'hcl'],
    'Arjun': [24, 'chennai', 'hcl'],
}

print(type(d))
"""

"""
    String Operations
"""

# info = "My name is \"Swadhikar\""
# info = 'My name is "Swadhikar"'
# print(info)
#
# info = """Python is a scripting Language
# that takes "minimum" time to learn"""

# info = '''Python is a scripting Language
# that takes "minimum" time to learn'''
# print(info)

# info = 'My name is \n\n\n"Swadhikar"'
# info = '''My name is
#
#
# swadhikar'''
# print(info)
"""
name = 'Saravana'
print(name)
print(name[0: 5])
print(name[-1])
print(name[::-1])   # reverse string
print(name[::-2])   # reverse string

print(name[50])
"""



"""
exists = 'world' in 'Hello world'   #Check for a substring
print(exists)


exists = 'a' in 'angel'
print(exists)



exists = 'a' in 'python'
print(exists)
"""
"""

text = "welcome to python Programming"
result = text.replace('Programming', 'Language')
#print(text.replace('P', 'p'))
#print(result)

# capitalize
print(text.capitalize())
print(text.title())
print(text.lower())
print(text.upper())

"""


concat_str = "Hi," + " hello" + '!' + "!!"
print(concat_str)


welcome_msg = 'Welcome {name}, good {message}!'

"""
greeting = welcome_msg.format('John', 'Evening')
print(greeting)
greeting = welcome_msg.format('Doe', 'Morning')
print(greeting)
"""
greeting = welcome_msg.format(message='Night', name='Rajan')
print(greeting)
