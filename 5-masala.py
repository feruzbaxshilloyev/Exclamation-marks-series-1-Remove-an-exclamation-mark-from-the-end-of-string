def remove(s):
    if s[-1] == '!':
        return s[:-1]
    return s

print(remove('salom!!!'))