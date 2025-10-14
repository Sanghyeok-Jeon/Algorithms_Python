data = list(input().split())

primitive_type = data[0]
for i in range(1, len(data)):
    tmp_data = data[i].replace(',', '').replace(';', '')
    tmp_type = ''
    tmp_name = ''
    for d in reversed(tmp_data):
        if d.isalpha():
            tmp_name += d
        else:
            if d == '[':
                tmp_type += ']'
            elif d == ']':
                tmp_type += '['
            else:
                tmp_type += d

    print(primitive_type + tmp_type, tmp_name[::-1] + ';')