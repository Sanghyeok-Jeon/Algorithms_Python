alpha_to_num = ['3', '2', '1', '2', '3', '3',
                '2', '3', '3', '2', '2', '1',
                '2', '2', '1', '2', '2', '2',
                '1', '2', '1', '1', '1', '2',
                '2', '1']

A = input()
B = input()

name_chem = ''.join([alpha_to_num[ord(A[i]) - ord('A')] + alpha_to_num[ord(B[i]) - ord('A')] for i in range(len(A))])
while True:
    if len(name_chem) == 2:
        break

    tmp_chem = ''
    for i in range(0, len(name_chem) - 1):
        new_num = (int(name_chem[i]) + int(name_chem[i + 1])) % 10
        tmp_chem += str(new_num)

    name_chem = tmp_chem

print(name_chem)
