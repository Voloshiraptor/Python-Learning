# Simple syntax and variable learning for strings

hello = "Hello World!"
print(hello)
# Concatenation test

my_name = "My name is Andre."
introduce_self = hello + " " + my_name
print(introduce_self)

# Testing print constructor
print(hello, my_name)

# Testing += concat
introduce_self_2 = introduce_self
introduce_self_2 += " I like to play Dota 2."
introduce_self_2 += " It is a very complex game requiring a wide variety of skills."
print(introduce_self_2)

# Multi-line string
introduce_self_3 = """
'Hello World! '
       " My Name is Andre "
I like to play Dota 2.

                    It is a very complex game requiring a wide variety of skills.
"""
print(introduce_self_3)

# NUMBERS PRACTICE
# Testing how Python handles numbers inside variables

test_int = 2
test_float = 2.1

# Testing if casting is needed on calculations
test_calculations = test_int + test_float
print(test_calculations)

test_calculations_2 = test_int / test_float

print(test_calculations_2)

# Modulo testing
test_calculations_3 = 65 % 2
print(test_calculations_3)
