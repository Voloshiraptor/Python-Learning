# Testing AND,OR,NOT
bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)

print(str(bool_one) + " " + str(bool_two) + " " + str(bool_three) + " " + str(bool_four) + " " + str(bool_five) )


# Testing If statement
def using_control_once():
    if 2+2 == 1+3:
        return "Success #1"


def using_control_again():
    if 2+2 and 1+3 == 3+1:
        return "Success #2"


print(using_control_once())
print (using_control_again())

#Elseif

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0


print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))


# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"

    elif 80 <= grade < 90:
        return "B"

    elif grade >= 70 and grade < 80:
        return "C"

    elif grade >= 65 and grade < 70:
        return "D"

    else:
        return "F"


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))

# Start coding here!
# raw_input not in pycharm
original = input("Enter a word: ")
# x.isalpha() checks to see if a string doesn't contain any non-letter characters
if len(original) > 0 and original.isalpha():
    print(original)
else:
    print('empty')