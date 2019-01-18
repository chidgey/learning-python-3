#!/usr/bin/env python3

"""Illustrates how Python can inherit from multiple classes at a time."""


class MySuperClass1():

    a = "MySuperClass1"

    def method_super1(self):
        print("method_super1 method called " + self.a)

    def method_super2(self):
        print("method_super2 method called " + self.a)


class MySuperClass2():

    b = "MySuperClass2"

    def method_super3(self):
        print("method_super3 method called " + self.b)

    def method_super4(self):
        print("method_super4 method called " + self.b)


class ChildClass(MySuperClass1, MySuperClass2):

    def child_method(self):
        print("child method")


c = ChildClass()
c.method_super1()
c.method_super2()
c.method_super3()
c.method_super4()
