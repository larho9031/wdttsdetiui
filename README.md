# wdttsdetiui

An interpreter for an esolang called Why Does This Towel Smell Different Each Time I Use It, commonly called WDTTSDETIUI or Towellang.

# the esolang

WDTTSDSETIUI's data structure consists of infinite stacks and a register called `mem`

`mem` starts at 0 and can be used to replace any value name in a command.

## the commands
- make
- push
- pop
- towel
- print
- letter
- add
- input
- while
- end

### make
`make X` makes a new stack with the name X
the name must be a number

__note: when putting `make A` into the program, it shows a syntax error on the wdttsdetiui program itself and not the interpreter__

### push
`push A X` pushes a value A onto stack X

### pop
`pop X` pops the top value of stack X

### towel
`towel A B` generates a value from A to B, then stores this into `mem`

### print & letter
`print X` prints the top value of stack X as a number

`print mem` prints mem as a number

`letter X` prints the top value of stack X as an ascii character

`letter mem` prints mem as an ascii character

### add
`add X` adds the top value of stack X with `mem` and stores the result back into `mem`

### input
`input` gets one byte of input from the user and overwrites `mem` with it

### while & end
`while X` - if the top value of stack X and `mem` are equal, jump to the matching `end` command

`end` - if the stack specified in the matching `while`'s top value and the value of `mem` aren't equal, jump back to the matching `while` command

## tips and tricks
1. You can load `mem` with whatever you want with the code below, assuming you have a stack already made:
```
push [value] 1
pop 1
```
2. You can subtract by using the `add` command with -1.
