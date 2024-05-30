s = input()

change_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for ca in change_alpha:
    s = s.replace(ca, '#')

print(len(s))