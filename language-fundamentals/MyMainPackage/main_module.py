def run():
    print('Hello from the main package')



if __name__ == "__main__":
    # tells us we are running this file directly from the shell and not importing.
    print('Running direct from the shell e.g. python main_module.py')
else:
    print('Main module imported')