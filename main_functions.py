import os
import sys

import settings

def helpmenu():
    print(settings.help_menu_text)

def compile(code, filename):
    pipe = os.popen("gcc -o {filename} -x c -".format(filename = filename), "w") # Open a file stream (which is actually to a process, but since everything is a file, it works) to our GCC command
    pipe.write(code) # Pipe the code into GCC (which is accepting code through stdin).
    pipe.close()

def save(code, filename): 
    code_save = open(filename, "w+")
    code_save.write(code) # Save the raw C code to the harddisk; we are not compiling.
    code_save.close()
