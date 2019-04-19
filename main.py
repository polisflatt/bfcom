#!/usr/bin/python3

import os
import sys

import interpret
import bftypes
import settings

from main_functions import *

argc = len(sys.argv[1:])

# Avoid exceptions
if (argc < 1):
    print("Too little arguments given...")
    helpmenu()
    exit(1)

sourcecode_filename = sys.argv[1]
arguments = sys.argv[2:]



def main():
    code_contents = open(sourcecode_filename)
    returned_c_code = interpret.interpret(code_contents.read())
    code_contents.close()

    polished_code = bftypes.c_code.format( # Polish the code by injecting the generated C code into it as well as the presets. 
            code = returned_c_code,
            memory_size = settings.memory_size
    )


    # Simple argument system. We don't need anything more.
    if (arguments[0] == "--compile" or arguments[0] == "-c"):
        compile(polished_code, arguments[1])
    
    elif (arguments[0] == "--save" or arguments[0] == "-s"):
        save(polished_code, arguments[1])
    
    elif (arguments[0] == "--print" or arguments[0] == "-p"):
        print(polished_code)
    
    else:
        helpmenu()


if __name__ == "__main__":
    main()