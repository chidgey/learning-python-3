#!/usr/bin/env python3

# note how we can override enter and exit to mop after using a resource, very handy.


class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        print("file is now open")
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()
        print("file is now closed")


with CustomOpen('using-pass-with-types.py') as f:
    contents = f.read()