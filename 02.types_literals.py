"""
2.2. Section 1 - Types of Literals in Python:
Python supports various types of literals, such as numeric literals, string literals, 
Boolean literals, and more. Let's explore different types of literals in Python with examples:
"""
#2.2.1. String Literals
# in single quote
x = 'stringforliterals'
print(x)

# in double quotes
y = "stringforliterals"
print(y)
# multi-line String
x = '''string 
           for 
               literals'''
print(x)

#2.2.2. Character Literals
# character literal in single quote
v = 'n'
print(v)

# character literal in double quotes
w = "a"
print(w)

#2.2.3. Number Literals
#They are immutable and there are three types of numeric
#literal (integer, float, complex)

## integer literal

# Binary Literals
a = 0b10100

# Decimal Literal
b = 50

# Octal Literal
c = 0o320

# Hexadecimal Literal
d = 0x12b

print(a, b, c, d)

## float literal
e = 24.8
f = 45.0

print(e, f)

## complex  literal
z = 7 + 5j

# real part is 0 here.
k = 7j

print(z, k)

#2.2.4. Boolean Literals
a = (1 == True)
b = (1 == False)
c = True + 3
d = False + 7

print("a is", a)
print("b is", b)
print("c:", c)
print("d:", d)

#2.2.5. Literal Collections
#Python provides four different types of literal 
# collections (List, Tuple, Dict, Set)

##List literal
number = [1, 2, 3, 4, 5]
topics = ['Biology', 'Physical', 'Programming', 2]
print(number)
print(topics)

##Tuple literal
year_number = (2020, 2021, 2022, 2023)
day_number = (1, 3, 5, 7)

print(year_number)
print(day_number)

##Dictionary literal
students = {'a': 'Alert', 'b': 'Bruno', 'c': 'Camila'}
information = {'address': '152, Call EEUU', 'age': 20, 'ID': 20}

print(students)
print(information)

##Set literal
vowels = {'a', 'e', 'i', 'o', 'u'}
fruits = {"apple", "banana", "cherry"}

print(vowels)
print(fruits)