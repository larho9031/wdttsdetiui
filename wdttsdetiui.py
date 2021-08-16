import random

# findMatching by Brain Damaged Senko#5942
# wdttsdetiui by Larho#9031
filepath = "program.wdttsdetiui"
debug = False # Gives info for each command executed

def findMatching(code, index, start="[", stop="]"):
    if code[index] == start:
        step = 1
    elif code[index] == stop:
        step =- 1
    else:
        return index
    depth=step
    while depth!=0:
        index += step
        if code[index] == start:
            depth += 1
        elif code[index] == stop:
            depth -= 1
    return index

codetemp = open(filepath, "r")
code = codetemp.readlines()
codetemp.close()
codetemp = None
pointer = 0
mem = 0
temp = 0
stacks = {}
loopcode = ""

def make(pointer, mem):
    try:
        temp = int(para)
    except ValueError:
        print("Line", pointer + 1, "- You cannot make stacks with a name other than a number")
        exit()
    else:
        stacks.update({para: []})

    if debug:
        print("Added stack named", para + ", with contents", stacks[para])
def push(pointer, mem):
    para = codetemp.split()[1]
    if para == "mem":
        para = mem
    try:
        para = int(para)
    except:
        print("Line", pointer + ": Somehow you're trying to push a string??")
        exit()
    stack = stacks[codetemp.split()[2]]
    stack.append(para)
    stacks.update({codetemp.split()[2]: stack})

    if debug:
        print("Stack named", codetemp.split()[2], "now has contents", stack)
def pop(pointer, mem):
    stack = stacks[para]
    try:
        mem = int(stack[-1])
    except IndexError:
        print("Line", pointer + 1, "- Cannot pop nothing")
        exit()
    stack.pop()
    stacks.update({para: stack})

    if debug:
        print("Stack named", para, "now has contents", stack)
        print("Mem is now", mem)
def prnt(pointer, mem):
    if para != "mem":
        stack = stacks[para]
        try:
            stack = stack[0]
        except IndexError:
            print("Line", pointer + 1, "- Cannot print an empty stack")
            exit()
    else:
        stack = mem
    if debug:
        if stack == mem:
            print("Mem is", mem)
        else:
            print("The top value on stack", para, "is", stack)
    else:
        if stack == mem:
            print(mem)
        else:
            print(stack)
def letter(pointer, mem):
    if para != "mem":
        stack = stacks[para]
        try:
            stack = stack[0]
        except IndexError:
            print("Line", pointer + 1, "- Cannot print an empty stack")
            exit()
    else:
        stack = mem
    if debug:
        if stack == mem:
            print("The ASCII character for mem is", chr(mem))
        else:
            print("The top value of stack", para, "as an ASCII character is", chr(stack))
    else:
        if stack == mem:
            print(chr(mem))
        else:
            print(chr(stack))
def towel(pointer, mem):
    if para == "mem":
        mem = random.randint(mem,int(codetemp.split()[2]))
    elif codetemp.split()[2] == "mem":
        mem = random.randint(int(para),mem)
    else:
        mem = random.randint(int(para),int(codetemp.split()[2]))
    if debug:
        print("Stored random number", mem, "in mem")
def inp(pointer, mem):
    mem = int(input("Input a number > "))
    if debug:
        print("Mem is now", mem)
def add(pointer, mem):
    stack = stacks[para]
    if debug:
        print("Added", str(stack[0]), "to mem")
def loop(pointer, mem):
    stack = stacks[para]
    if mem != stack[0]:
        pointer = findMatching(loopcode, pointer)
        if debug:
            print("Jumped forward to line", pointer + 1)
def end(pointer, mem):
    para = code[findMatching(loopcode, pointer)].split()[1]
    stack = stacks[para]
    if mem == stack[0]:
        pointer = findMatching(loopcode, pointer)
        if debug:
            print("Jumped backwards to line", pointer + 1)

glt = {
    "make": make,
    "push": push,
    "pop": pop,
    "towel": towel,
    "print": prnt,
    "letter": letter,
    "add": add,
    "input": inp,
    "while": loop,
    "end": end
}

for i in code:
    if i.split()[0] == "while":
        loopcode += "["
    elif i.split()[0] == "end":
        loopcode += "]"
    else:
        loopcode += "-"
    if i[-1] == "\n":
        code[temp] = (code[temp])[:-1]
    temp += 1

while True:
    try:
        codetemp = code[pointer]
    except:
        break

    try:
        arg = codetemp.split()[0]
    except IndexError:
        arg = ""
    if len(codetemp.split()) > 1:
        para = codetemp.split()[1]

    if arg in glt:
        glt[arg](pointer, mem)
    elif arg == "":
        pass
    else:
        print("Line", pointer + 1, "- Invalid command", arg)
        exit()
    pointer += 1
exit()
