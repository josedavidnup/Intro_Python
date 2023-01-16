# python 10_float.py
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

y_str = format(y, '.2g')
print(y_str)
print(str(x) == y_str) 

print('*' * 10)

print(y, x)

tolerancia = 0.00001

print(abs(x - y) < tolerancia)

y = round((1.1 + 2.2),1) 
print(y)