N = int(input())
bit_before = list(input())
bit_after = list(input())

if N % 2:
    for b in range(len(bit_before)):
        if bit_before[b] == '0':
            bit_before[b] = '1'
        else:
            bit_before[b] = '0'

if bit_before == bit_after:
    print('Deletion succeeded')
else:
    print('Deletion failed')