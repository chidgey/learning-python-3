#!/usr/bin/env python3

"""Example of sorting custom objects with lamdas and custom string formatting on print."""

class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def __repr__(self):
        return self.__str__()

    # special method: string representation of this object
    def __str__(self):
        return "{0}:{1}:{2}".format(self.name, self.salary, self.age)

    # special method: length of this object
    def __len__(self):
        return self.age

    # special method: destructor, last chance to release resources.
    def __del__(self):
        print("instance destroyed")

# populate a few objects
e1 = Employee("Tom", 20000, 32)
e2 = Employee("Jane", 50000, 36)
e3 = Employee("Bob", 45000, 40)

emp_list = [e2, e3, e1]

# because we defined str above, we have a custom string formatter for the output
print("\nunsorted employees")
print(emp_list)

# use of special method - pick a sensible value for len, h
print(len(e1))

print("\nsort Employee objects by name")
print(sorted(emp_list, key=lambda x: x.name)) 

print("\nsort Employee objects by age")
print(sorted(emp_list, key=lambda x: x.age)) 

print("\nsort Employee objects by salary")
print(sorted(emp_list, key=lambda x: x.salary)) 

# now all instances fall out of scope and are garbage collected, thus calling
# __del__ on each.