def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_number = []
    bottom_numbers = []
    operators = []
    results = []

    for expr in problems:
        parts = expr.split()
        if len(parts) != 3:
            return 'Error: Invalid format.'
        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        top_number.append(num1)
        bottom_numbers.append(num2)
        operators.append(operator)

        if show_answers:
            if operator == '+':
                results.append(str(int(num1) + int(num2)))
            else:
                results.append(str(int(num1) - int(num2)))

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for i in range(len(operators)):
        length = max(len(top_number[i]), len(bottom_numbers[i])) + 2
        line1 += top_number[i].rjust(length) + ('    ' if i < len(operators) - 1 else '')
        line2 += operators[i] + bottom_numbers[i].rjust(length - 1) + ('    ' if i < len(operators) - 1 else '')
        line3 += '-' * length + ('    ' if i < len(operators) - 1 else '')
        if show_answers:
            line4 += results[i].rjust(length) + ('    ' if i < len(operators) - 1 else '')

    arranged = line1 + '\n' + line2 + '\n' + line3
    if show_answers:
        arranged += '\n' + line4

    return arranged



print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"],1)}')


