def count_cut_pieces(expression):
    stack = []
    total_pieces = 0

    for i in range(len(expression)):
        if expression[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if expression[i - 1] == '(':
                total_pieces += len(stack)
            else:
                total_pieces += 1

    return total_pieces

expression = input()
result = count_cut_pieces(expression)

print(result)