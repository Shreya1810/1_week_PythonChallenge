'''Day 2: Conditional Statements*
Write a Python program that asks the user to enter a number and then checks if the number is even or odd. Print an appropriate message based on the result.'''

num = int(input('Enter a number : '))

if num % 2 == 0:
  print("Yes, even")
else:
  print('OOps odd number!')