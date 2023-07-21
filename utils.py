import sys, re

def get_command_line_arguments() -> list:
    return sys.argv[1:]

def normalize_equation(equation: str) -> str:
    result = []
    inside_parentheses = False

    for char in equation:
        if char.isalpha():
            result.append(char)
        elif char == '(':
            inside_parentheses = result and result[-1] == '-'
        elif char == ')':
            inside_parentheses = False
        elif inside_parentheses:
            result.append('-' if char == '+' else '+')
        else:
            result.append(char)

    return ''.join(result)

def split_equation(equation: str) -> list:
    variables = {variable: None for variable in equation if variable.isalpha()}
    words = re.findall(r'[A-Z]+', equation)
    operands, result = words[:-1], words[-1]
    operators = re.findall(r'[+\-*]', equation)
    operators[:0] = ['+']
    return [variables, operators, operands, result]

def create_subproblem(operands, operators, result):
    subproblems = {}
    impact = {}
    
    max_subprob_length = max(len(result), max(len(operand) for operand in operands))
    for operand, operator in zip(operands, operators):
        for i, letter in enumerate(operand):
            subprob_index = max_subprob_length - len(operand) + i
            impact.setdefault(subprob_index, {}).setdefault(letter, [0, 0])
            impact[subprob_index][letter][operator == '-'] += 1
            subproblems.setdefault(subprob_index, set()).add(letter)

    for i, letter in enumerate(result):
        subprob_index = i
        impact.setdefault(subprob_index, {}).setdefault(letter, [0, 0])
        impact[subprob_index][letter][1] += 1
        subproblems.setdefault(subprob_index, set()).add(letter)

    return [list(subproblems[i]) for i in range(len(subproblems) - 1, -1, -1)], [impact[i] for i in range(len(impact) - 1, -1, -1)]
