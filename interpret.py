import bftypes

def interpret(code):
    result = "" # Resulting C Code

    for line in code.splitlines():
        for char in line: # Processing
            try:
                if (not char in bftypes.main_symbols): # Do not throw an error if the symbol is not found in the dictionary.
                    continue

                result += bftypes.main_symbols[char] + "\n" # Resolving every brainf**k character to its C equivalent
            except Exception as specific_ex: # Tell the user what exception has occured.
                print("Exception has occured")
                print("{exception}".format(exception = specific_ex))
            
    return result
    