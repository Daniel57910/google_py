import re

a = 'abcde 123'
b = list(filter(lambda char: (char.isalnum()), a))
print ''.join(b)
print a
c = re.findall(r'([a-z]|[0-9])', a)
print ''.join(c)