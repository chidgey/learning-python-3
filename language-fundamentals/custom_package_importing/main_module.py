def run():
    print('Hello from custom_package_importing.main_module')


if __name__ == "__main__":
    # tells us we are running this file directly from the shell and not importing.
    print('Running direct from the shell e.g. python custom_package_importing')
else:
    print('"custom_package_importing" has been imported.')
