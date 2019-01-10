# https://www.programiz.com/python-programming/directory
# https://dbader.org/blog/python-file-io

import os


def printCurrentWorkingDirectory():
    """Print the current working directory"""
    path = os.getcwd()
    print("The current working directory is %s" % path)


def createNewDirectory():
    """Create a new directory in the current working directory"""
    newDirectoryPath = os.getcwd() + '/myProject'
    # readable and accessible by all users, only writable by the owner.
    newDirectoryAccessRights = 0o755
    try:
        os.mkdir(newDirectoryPath)
        os.chmod(newDirectoryPath, newDirectoryAccessRights)
    except OSError:
        print("Creation of the directory %s failed" % newDirectoryPath)
    else:
        print("Successfully created the directory %s " % newDirectoryPath)


def createNewDirectoryWithSubDirectories():
    """Creates a directory which has other nested directories"""
    newDirectoriesPath = os.getcwd() + '/project1/project2/project3'
    try:
        os.mkdirs(newDirectoriesPath)
    except OSError:
        print("Creation of the directory %s failed" % newDirectoriesPath)
    else:
        print("Successfully created the directory %s " % newDirectoriesPath)


def createNewDirectoryPrompt(promptMsg='Are you sure you want to create a directory (y or n)? '):
    """Create a new folder, or prompt the user to replace if it already exists."""
    retries = 3

    while True:
        ok = input(promptMsg)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print('Please try again!')


printCurrentWorkingDirectory()
createNewDirectory()
createNewDirectoryWithSubDirectories()
createNewDirectoryPrompt()

# continue this class of basic things
# https://stackabuse.com/creating-and-deleting-directories-with-python/

# interesting python things
# concurrent execution threads, queues and async i/o things
# structured markup processing tools - for scraping
# mailbox reading and manipulation.
# data compression
# data persistence
# stat - for fstat details, on file handles etc...
# argparse for argument parsing
# https://www.stavros.io/tutorials/python/

# create a web scraper
# https://code.tutsplus.com/courses/crawl-the-web-with-python