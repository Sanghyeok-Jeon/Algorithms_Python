def convert_style(name):
    if name[0] == '_' or name[-1] == '_' or '__' in name:
        return 'Error!'

    if '_' in name and any(c.isupper() for c in name):
        return 'Error!'

    if '_' in name:
        result = ''
        upper = False
        for ch in name:
            if ch == '_':
                upper = True
            else:
                result += ch.upper() if upper else ch
                upper = False
        return result

    elif any(c.isupper() for c in name):
        if name[0].isupper():
            return 'Error!'
        result = ''
        for ch in name:
            if ch.isupper():
                result += '_' + ch.lower()
            else:
                result += ch
        return result

    else:
        return name

print(convert_style(input()))