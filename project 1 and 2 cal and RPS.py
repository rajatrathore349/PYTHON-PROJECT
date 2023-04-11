`'''
# project 1 : to make calculator
age = input('enter your age please = ', )
# string
print(age)
name = 'rajat'
print(name)
# integers
number = 526
# float
num = 52.86
# print all the variables
print(name, number, num)

# day 4
age = 50
if age < 20:
  print('age is less than 20')
elif age > 20:
  print('age is greater than 20')
elif age > 25:
  print('age is greater than 25')

fruit = ' apple'
if fruit == 'apple':
  print('i got apple from the market')
elif fruit == 'banana':
  print('i got banana from the market')
elif fruit == 'watermelon':
  print('i got watermelon from the market')
else:
  print('u r not for anything')

# to make the calculator

# process 1: take input from the user
# input : numbers/operands and operator
operand1 = input('please enter number 1: ')
operand2 = input('please enter number 2: ')

# lets check the nature of operands
print(type(operand1), type(operand2))

# changing conversion
# type conversion = changing the data type of one variable to another

# LHS = RHS
# STEP1 = FIRST SOLVE THE OR EVLUTATE RHS
# STEP2 = THEN ASSIGEN RHS TO LHS

operand1 = int(operand1)
operand2 = int(operand2)

# let's check the nature of operands
print(type(operand1), type(operand2))

# lets add the operands
result = operand1 + operand2

# let's print the results
print(' the result is:', result)


# TAKE THE INPUT OF OPERATOR AND operand1

number1 = input('please enter the number 1: ')
number2 = input('please enter the number 2: ')
operator = input('enter the operator: ')

number1 = int(number1)
number2 = int(number2)
if operator == '+':
  result = number1 + number2
elif operator == '-':
  result = number1 - number2
elif operator == '*':
  result = number1 * number2
elif operator == '/':
  result = number1 / number2

#let's print the value of the result

print('the result is: ', result)

number1 = input('please enter the number 1: ')
number2 = input('please enter the number 2: ')
operator = input('enter the operator: ')

number1 = int(number1)
number2 = int(number2)
if operator == '+':
  result = number1 + number2
elif operator == '-':
  result = number1 - number2
elif operator == '*':
  result = number1 * number2
elif operator == '/':
  result = number1 / number2
else:
  result = 'not defined'
#let's print the value of the result
print('the result is: ', result)

# project 2: paper rock scissors

user = input('pick your move[ paper,rock,sessior]: ')
computer = input('pick computer choice[ paper,rock,sessior]: ')

#let's print
print (user,computer)


# project 2: paper rock scissors

user = input('pick your move[ paper,rock,sessior]: ')
computer = input('pick computer choice[ paper,rock,sessior]: ')

#let's print
print (user,computer)

user_choice = input('choose the user weapon{rock,paper,sessior}: ')
computer_choice = input('choose the computer weapon{rock,paper,sessior}: ')

print(user_choice,computer_choice)

number1 = 2
number2 = 5

print(number1== 2)
print(number2== 5)
print(number1== 5)
print(number2== 1)

# working of and operator

print(number1== 2 and number2== 5)
print(number1== 3 and number2== 5)
print(number1== 2 and number2== 3)
print(number1== 5 and number2== 5)


numberx = 52
numbery = 67

print(numberx== 52 and numbery== 67)
print(numberx== 67 and numbery== 67)
print(numberx== 52 and numbery== 52)
print(numberx== 12 and numbery== 67)
print(numberx== 52 or numbery== 67)
print(numberx== 67 or numbery== 67)
print(numberx== 52 or numbery== 52)
print(numberx== 12 or numbery== 61)


#importing the random module
import random

# lets create the game of paper rock sessior
user_choice = input('choose the user weapon{rock,paper,sessior}: ')

#this is command wiil pick a string randomly from 'rock' 'sessior', 'paper'
#and it assign to computer choice

computer_choice = random.choice(['rock', 'paper', 'sessior'])

if user_choice == 'rock' and computer_choice == 'rock':
  print(user_choice, computer_choice)
  print('Draw')

elif user_choice == 'rock' and computer_choice == 'paper':
  print(user_choice, computer_choice)
  print('computer_choice won')
elif user_choice == 'paper' and computer_choice == 'sessior':
  print(user_choice, computer_choice)
  print('computer_choice won')
elif user_choice == 'paper' and computer_choice == 'rock':
  print(user_choice, computer_choice)
  print('user_choice won')
elif user_choice == 'rock' and computer_choice == 'sessior':
  print(user_choice, computer_choice)
  print('user_choice won')
elif user_choice == 'paper' and computer_choice == 'paper':
  print(user_choice, computer_choice)
  print('Draw')
elif user_choice == 'sessior' and computer_choice == 'rock':
  print(user_choice, computer_choice)
  print('computer_choice won')
elif user_choice == 'sessior' and computer_choice == 'paper':
  print(user_choice, computer_choice)
  print('user_choice won')
elif user_choice == 'sessior' and computer_choice == 'sessior':
  print(user_choice, computer_choice)
  print('Draw')

user_choice = input('choose the user weapon{rock,paper,sessior}: ')
import random

computer_choice = random.choice(['rock', 'paper', 'sessior'])

if user_choice == 'paper' and computer_choice == 'sessior':
  print(user_choice, computer_choice)
  print('computer wins')
elif user_choice == 'paper' and computer_choice == 'paper':
  print(user_choice, computer_choice)
  print('draw')

# let's pratice of calculator

number1 = input('enter the first number: ')
number2 = input('enter the number second: ')
operator = input('enter the operator: ')
      
number1 = int(number1)
number2 = int(number2)

if operator == '+':
  result = number1 + number2
elif operator == '-':
  result = number1 - number2
elif operator == '*':
  result = number1 * number2
elif operator == '/':
  result = number1 / number2

print('the result is:', result)


number1 = input('enter the number first: ')
number2 = input('enter the number second: ')
operator = input('the operator sign: ')
number1 = int(number1)
number2 = int(number2)
if operator == '+':
  result = number1 - number2
elif operator == '-':
  result = number1 + number2
elif operator == '*':
  result = number1 / number2
elif operator == '/':
  result = number1 * number2

print('the result is: ', result)

import random
user_choice = input('choose your weapon(rock,sessior,paper): ')
computer_choice = random.choice(['rock','paper','sessior'])
if user_choice == 'paper' and computer_choice == 'paper':
  print(user_choice, computer_choice)  
  print('draw')
elif user_choice == 'paper' and computer_choice == 'sessior':
  print(user_choice, computer_choice)
  print('computer wins')
elif user_choice == 'paper' and computer_choice == 'rock':
  print(user_choice, computer_choice)
  print('user wins')
elif user_choice == 'sessior' and computer_choice == 'paper':
  print(user_choice, computer_choice)
  print('user wins')
elif user_choice == 'sessior' and computer_choice == 'rock':
  print(user_choice, computer_choice)
  print('computer wins')
elif user_choice == 'sessior' and computer_choice == 'sessior':
  print(user_choice, computer_choice)
  print('draw')
elif user_choice == 'rock' and computer_choice == 'paper':
  print(user_choice, computer_choice)
  print('computer wins')
elif user_choice == 'rock' and computer_choice == 'sessior':
  print(user_choice, computer_choice)
  print('user wins')
elif user_choice == 'rock' and computer_choice == 'rock':
  print(user_choice, computer_choice)
  print('draw')
  '''

# project of calculator

number A = input('please enter the number A: ')
number B = input('please enter the number B: ')
operator = input('operator sign: ')

number A = int('number A')
number B = int('number B')

if














