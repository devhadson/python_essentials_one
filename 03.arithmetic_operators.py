# 2.3. Section 3 - Operators - data manipulation tools
# Types of Operators in Python: Arithmetic Operators, Comparison 
# Operators, Logical Operators, Bitwise Operators, Assignment 
# Operators, Identity Operators and Membership Operators.
"""
2.3.1. Arithmetic Operators:

Operator	Description	                                                                    Syntax
+	        Addition: adds two operands	                                                    x + y
–	        Subtraction: subtracts two operands	                                            x – y
*	        Multiplication: multiplies two operands	                                        x * y
/	        Division (float): divides the first operand by the second	                    x / y
//	        Division (floor): divides the first operand by the second	                    x // y
%	        Modulus: returns the remainder when the first operand is divided by the second	x % y
**	        Power: Returns first raised to power second	                                    x ** y
"""

# Division (float):
print(5/5)
print(10/2)
print(-10/2)
print(20.0/2)

# Division (floor)
print(10//3)
print (-5//2)
print (5.0//2)
print (-5.0//2)

a = 9
b = 4

add = a + b
sub = a - b
mul = a * b
mod = a % b
p = a ** b

print('add', add)
print('sub', sub)
print('mul', mul)
print('mod', mod)
print('p', p)

"""
2.3.2. Comparison Operators

Operator	Description	                                                                            Syntax
>	        Greater than: True if the left operand is greater than the right	                    x > y
<	        Less than: True if the left operand is less than the right	                            x < y
==	        Equal to: True if both operands are equal	                                            x == y
!=	        Not equal to – True if operands are not equal	                                        x != y
>=	        Greater than or equal to True if the left operand is greater than or equal to the right	x >= y
<=	        Less than or equal to True if the left operand is less than or equal to the right	    x <= y
"""
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)