'''*Day 5: Functions*
Define a function that calculates the factorial of a number. Ask the user for a number and then call the function to compute and print its factorial'''

def factorial(number):
  if number == 1:
    return (number)

  return number * factorial(number - 1)

number = int(input("Enter the number to calculate the factorial: "))
if number < 0:
  print("Sorry, factorial doesn't exist for negative number")
elif number == 0:
  print("The factorial of 0 is 1")
else:
  print(factorial(number))