from operator import add, sub, mul, truediv
from fractions import Fraction
# import sys,os
# sys.path.append(os.getcwd())
from pystack import Stack

def main():
    exp = input('exp: ')
    val = eval_exp(exp)
    print(f'val: {val}')


op_map = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


def convert(exp):
    for it in reversed(exp.split(' ')):
        if it in op_map:
            yield True, op_map[it]
        else:
            yield False, Fraction(it)


def eval_exp(exp):
    stack = Stack()

    for is_op, it in convert(exp):
        if is_op:
            left = stack.pop()
            right = stack.pop()
            stack.push(it(left, right))
        else:
            stack.push(it)
    return stack.pop()


if __name__ == '__main__':
    main()
    # exp: + 5 - 2 * 3 / 4 7
    # val: 37/7
