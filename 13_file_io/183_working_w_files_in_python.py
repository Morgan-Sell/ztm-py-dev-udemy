# Working w/ Files in Python

"""
NOTES:
-----
- Most of the time, machines are NOT working in one environment.
  ** e.g., connect to a database or API
- Use I/O to compress images.

- open() uses a cursor allowing the file to only be read once.
  ** Once the file is opened, a file object is returned.

- seek(idx_num) moves the cursor to the selected index number. 

- readline() moves down the text file reading each line of text.

- readlines() returns a list. Each element of the list is a line from the text file.

- Use close() to manually close the file and allow access to the file via another program.

EXAMPLE CODE:
------------

my_file = open("test.txt")

print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.read())

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

print(my_file.readlines())

my_file.close()

"""