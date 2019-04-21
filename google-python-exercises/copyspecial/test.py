import re
regex = r'(\w+)__(\w+)__.+([txt]|[jpg])'
test_file = 'hello__dog__.txt'
fail_file = 'hello_world.png'
good_match = re.search(regex, test_file)
bad_match = re.search(regex, fail_file)
print good_match.group()
print bad_match