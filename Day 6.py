'''*Day 6: File Handling*
Create a text file with some content. Write a Python program that reads the content of the file and displays it on the screen.'''

f = open('file.txt','r')
print(f.read())