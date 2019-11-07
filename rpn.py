#!/usr/bin/env python3

import operator
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)

        print(colored(stack, "yellow"))
    if len(stack) != 1:
        raise TypeError(colored("Too many parameters", "red"))
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print(colored("Result: ", "green"), colored(result, "green"))

if __name__ == '__main__':
    main()
