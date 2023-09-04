'''*Day 7: Mini Project*
Choose a small project to work on. It could be a simple to-do list, a calculator, or any other idea you have in mind. Spend some time planning and coding this project using the Python skills you've learned over the week.
'''

# To do list
print("Welcome to the Simple To-Do List App!")
print("Menu")
print("1. Add a Task\n2. View all Tasks\n3. Remove a task\n4. Quit")

while True:
  choice = int(input("Please Enter you choice : "))
  if choice == 1:
    title = input("Enter task title : ")
    n = int(input("Enter number of items to add: "))
    task = [input() for _ in range(n)]
    print(f"Task {title} added!")
  elif choice == 2:
    print(f"{title} - {task} ")
  elif choice == 3:
    remove = input('Enter a task title to remove: ')
    task.clear()
    print(f"{title} has been removed.")
  else:
    break 
print("Goodbye!")  