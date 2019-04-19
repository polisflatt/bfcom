## bfcom

### *A compiler for the (joke) language BrainFuck*

Bfcom is a very simple compiler which aims to compile standardized brainfuck. That is, it only seeks to compile features integral to what brainfuck is normally known for. For this reason, this compiler will not be adding in any other features.

It works by emulating memory using arrays. For instance, if I want to advance one address, I would just type *>* and it would effectively translate to *i++;* in C. This means that the pointer is now pointing to the next array element, effectively emulating memory, which brainfuck requires.

    char array[memory_size];
    char* i = &array;

For a comparison of brainfuck to C, see this list below:

"> : `i++;`"
"< : `i--;`"
"+ : `(*i)++;`"
"-: `(*i)--;`"


The compiler uses Python to loop through a brainfuck file, then it translates to C. Other options within the compiler (or, rather, shall I be calling it: the translator) can use GCC to compile it.

This is nothing really special or grandiose, but it can be useful for testing and experimental purposes, if you do not want to use a JavaScript version of brainfuck. However, this program was only made as an experiment, and thus will not be updated. 
