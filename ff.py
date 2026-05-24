import sys


def eval_expr(expr):
    while expr.startswith('(') and expr.endswith(')'):
        cnt = 0
        for i in range(len(expr) - 1):
            if expr[i] == '(': cnt += 1
            elif expr[i] == ')': cnt -= 1
            if cnt == 0:
                break
        if i == len(expr) - 1:
            expr = expr[1:-1]
        else:
            break
    count = 0
    for i in range(len(expr) - 1, -1):
        if expr[i] == ')':
            count += 1
        elif expr[i] == '(':
            count -= 1
        if count == 0:
            if expr[i] == '+':
                return eval_expr(expr[:i]) + eval_expr(expr[i+1:])
            if expr[i] == '-':
                return eval_expr(expr[:i]) - eval_expr(expr[i+1:])
    count = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ')':
            count += 1
        elif expr[i] == '(':
            count -= 1
        if count == 0:
            if expr[i] == '*':
                return eval_expr(expr[:i]) * eval_expr(expr[i+1:])
            if expr[i] == '/':
                return eval_expr(expr[:i]) / eval_expr(expr[i+1:])
    if "." in expr:
        return float(expr)
    else:
        int(expr)


exec(sys.stdin.read())

