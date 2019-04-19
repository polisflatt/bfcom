import settings


c_code = """
#include <stdio.h>


int main(void)
{{

    char array[{memory_size}]; /* This char array is imaginary memory. */
    char* i = array; /* This pointer is pointing to 1 byte in the array of memory_size bytes. */

    {code}

    return 0;
}}
"""

main_symbols = {
    "+":"(*i)++;",
    "-":"(*i)--;",
    ">":"i++;",
    "<":"i--;",
    ".":"putchar(*i);",
    ",":"*i = getchar();",
    "[":"while (*i != '\\0') {", # What is interesting about this is the fact that it is not exactly compatible with getchar(), as getchar() returns EOF (which is -1) and not NULL. Ergo, getchar() won't ever terminate with brainf**k.
    "]":"}", # Cheap way to have a while field. It works because I am abiding by the brainf**k standard.
    " ":""
} # Not even Lexical Analysis, just minor translations of code. That's why I started with BrainF**K