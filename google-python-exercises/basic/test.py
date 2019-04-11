a = 'abcde 123'
b = list(filter(lambda char: (char.isalnum()), a))
print ''.join(b)