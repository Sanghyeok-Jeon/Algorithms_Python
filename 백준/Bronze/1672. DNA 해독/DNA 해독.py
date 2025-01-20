def char_to_num(chr):
    if chr == 'A':
        return 0
    elif chr == 'G':
        return 1
    elif chr == 'C':
        return 2
    else:
        return 3

DNA_table = ['ACAG',
             'CGTA',
             'ATCG',
             'GAGT']

N = int(input())
N_seq = list(input())

while True:
    if len(N_seq) == 1:
        print(*N_seq)
        break

    len_seq = len(N_seq)

    An_1 = N_seq[len_seq-2]
    An = N_seq[len_seq-1]

    N_seq[len_seq-2:len_seq] = DNA_table[char_to_num(An_1)][char_to_num(An)]