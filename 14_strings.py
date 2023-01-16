# python 14_strings.py
text = 'Ella sabe programar en Python'
''''
print('JavaScript' in text)
print('Python' in text)
print('python' in text)

if ('Python' in text):
  print('Elegiste bien')
else:
  print('Tambien elegiste bien')
'''
size = len(text)

print(size)

print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))

print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('rust'))
print(text.replace('Python', 'Go'))

text2 = 'este es un titulo'

print(text2)
print(text2.capitalize())
print(text2.title())
print(text2.isdigit())
print(text2.isdigit())
print('123'.isdigit())
