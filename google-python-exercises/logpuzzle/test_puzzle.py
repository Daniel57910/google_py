test_file = 'test/puzzle/name.jpg'
fail_file = 'test/no/n.png'

if 'puzzle' in test_file:
  print('basic regex')

if 'puzzle' not in fail_file:
  print('basic regex working')