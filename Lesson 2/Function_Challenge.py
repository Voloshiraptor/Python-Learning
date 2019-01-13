# Code challenges on CodeAcademy lesson 2 for functions

# Challenge 1
# Write your average function here:
def average(num1,num2):
  return (num1+num2)/2
# Uncomment these function calls to test your average function:
print(average(1, 100))
 #The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# Challenge 2
# Write your tenth_power function here:
def tenth_power(num):
  return num**10
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# Challenge 3
# Write your introduction function here:
def introduction(first_name,last_name):
  return last_name + ", " + first_name + " " + last_name
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# Challenge 4
# Write your square_root function here:
def square_root(num):
  return num**.5
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# Challenge 5
# Write your tip function here:
def tip(total,percentage):
    return total*(percentage/100)
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# Challenge 6
# Write your win_percentage function here:
def win_percentage(wins,losses):
  return wins/(wins+losses) *100
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# Challenge 7
# Write your first_three_multiples function here:
def first_three_multiples(num):
  print(num)
  print(num*2)
  print(num*3)
  return num*3

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# Challenge 8
# Write your dog_years function here:
def dog_years(name,age):
  return name + ", you are " + str(age*7) + " years old in dog years"
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# Challenge 9
# Write your remainder function here:
# The function should return the remainder of twice num1 divided by half of num2.
def remainder(num1,num2):
  return ((2*num1)%(num2/2))
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

# Challenge 10
# Write your lots_of_math function here:
# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function
# should print 3 lines and return 1 value.

# First, the sum of a and b.
# Second, d subtracted from c.
# Third, the first number printed, multiplied by the second number printed.
# Finally, it should return the third number printed mod a.

def lots_of_math(a,b,c,d):
  one= a+b
  two=d-c
  three=one*two
  print(one)
  print(two)
  print(three)
  return three % a
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

