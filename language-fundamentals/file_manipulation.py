#!/usr/bin/env python3

"""Manipulating files on disk with simple text file manipulation."""

# make sure you are in the right directory in the terminal before running this.
myfile =  open('file_manipulation_read.txt')

# read the file content, from the beginning to end
fileContent = myfile.read()
print(fileContent)

# second read returns nothing, as we are at the end
fileContent = myfile.read()
print(fileContent)

# reset the cursor back to the start of the file
myfile.seek(0)

# so we can read it again
fileContent = myfile.readlines()
print(fileContent)

# you need to close files when you are done with them
myfile.close()

# this is a better way to use and close the file resource
with open('file_manipulation_read.txt', mode='r') as my_new_file:
    contents = my_new_file.read()

print(contents)

# writing to a new file
with open('file_manipulation_write.txt', mode='w') as myfile:
    contents = myfile.write('Welcome to the new file! Please refer to file_manipulation.py')
    # myfile.read() this will throw an error

# append only - good for logs
with open('file_manipulation_write.txt', mode='a') as myfile:
    contents = myfile.write('\nTHIS WAS APPENDED')
    # myfile.read() this will throw an error

# reading and writing to an existing file
with open('file_manipulation_write.txt', mode='r+') as myfile:
    contents = myfile.write('...OVERWRITTEN...')
    myfile.read() # all good we can read too.

# writing a new file and allows reading
with open('file_manipulation_overwrite.txt', mode='w+') as myfile:
    contents = myfile.write('overwrites existing and allows reading too')
    myfile.read() # all good we can read too.
