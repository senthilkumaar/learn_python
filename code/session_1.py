"""String datatype"""
name = 'Saravana'
print(name)
print(type(name))

"""List datatype"""
l = ["Saravana","rajesh", "Murugan", "Vivek", 1, 3, "arjun", 1.5]
print(l)
print(type(l))

"""Tuple datatype"""
t = ("Saravana","rajesh", "Murugan", "Vivek", 1, 3, "arjun", 1.5)
print(t)
print(type(t))

pi = 314
print(pi)
print(type(pi))

"""Dict datatype"""
d = {
    # 'Swad': 29, 'Rajesh': 27, 'Arjun': 24
    'Swad': [29, 'chennai', 'hcl'],
    'Rajesh': [27, 'chennai', 'hcl'],
    'Arjun': [24, 'chennai', 'hcl'],
}
print(d)
print(type(d))

"""
    String Operations
"""

# Double quoted vs single quoted string
info = "My name is \"Swadhikar\""
info = 'My name is "Swadhikar"'
print(info)

# Multiline string
info = """Python is a scripting Language
that takes "minimum" time to learn"""
print(info)

info = '''Python is a scripting Language
that takes "minimum" time to learn'''
print(info)

# Bad usage of \n newline character
info = 'My name is \n\n\n"Swadhikar"'
info = '''My name is


swadhikar'''
print(info)

"""String Slicing"""

name = 'Saravana'
print(name)
print(name[0: 5])   # name[0 to 4th]
print(name[-1])     # last character
print(name[::-1])   # reverse string
print(name[::-2])   # reverse string
print(name[50])     # IndexError: List index out of range


"""Searching a character in string"""
exists = 'a' in 'python'
print(exists)

# Relace method
text = "welcome to python Programming"
result = text.replace('Programming', 'Language')
print(text.replace('P', 'p'))
print(result)

# capitalize, title, lower and upper()
print(text.capitalize())
print(text.title())
print(text.lower())
print(text.upper())

# String concatenation
concat_str = "Hi," + " hello" + '!' + "!!"
print(concat_str)

# String formatting usual way
welcome_msg = 'Welcome {}, good {}!'

greeting = welcome_msg.format('John', 'Evening')
print(greeting)
greeting = welcome_msg.format('Doe', 'Morning')
print(greeting)

# String formatting using keyword
welcome_msg = 'Welcome {name}, good {message}!'
greeting = welcome_msg.format(message='Night', name='Rajan')
print(greeting)
