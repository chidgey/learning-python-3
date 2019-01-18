#!/usr/bin/env python3

"""Illustrates how Python can make class methods static."""


class Music:

    # STATIC CLASS ATTRIBUTE - defined for all instances
    instrument = "piano"

    # CLASS METHOD, the same for any instance of a class
    @staticmethod
    def play():
        '''This will appear in the static method documentation for the class'''
        print("*playing music*")

    # INSTANCE METHOD, defined with self. This has no args, effectively void.
    def stop(self):
        '''This will appear in the instance documentation for the class'''
        print("stop playing: " + self)


Music.play()

# this method is instance only
# Music.stop()

obj = Music()
obj.stop()

# the inbuilt help method is great for inspecting objects
help(Music)
