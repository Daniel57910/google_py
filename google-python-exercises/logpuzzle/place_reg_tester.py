import sys
import re
example = 'http: // code.google.com/edu/languages/google-python-class/images/puzzle/p-bija-baei.jpg'
reg = r'\p-(\w+)-(\w+)'

word = re.search(reg, example).group(2)
print(word)
