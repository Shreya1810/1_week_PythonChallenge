'''Day 4: Lists*
Write a Python program that creates a list of your favorite fruits. Then, use a for loop to print each fruit in the list'''

fruits_list = ['grapes', 'banana', 'dragon fruit', 'papaya', 'pineapple', 'custurd apple']

print('Your favourite fruits are as shown below: ')

for i, fruit in enumerate(fruits_list):
  print(i, fruit)