import re

test_string = '<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>'
words = re.findall(r'<td>(\w+)</td>', test_string)
print words
