N = int(input())
channels = list(input() for _ in range(N))

idx_kbs1 = channels.index('KBS1')

print('1' * idx_kbs1, end='')
print('4' * idx_kbs1, end='')

channels.remove('KBS1')
channels = ['KBS1'] + channels

idx_kbs2 = channels.index('KBS2')

print('1' * idx_kbs2, end='')
print('4' * (idx_kbs2 - 1))