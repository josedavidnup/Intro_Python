#python 07_transformation.py
name = 'jose'
print(type(name))
name = 12
print(type(name))
name = True 
print(type(name))
print('Jose ' + 'Nunez')
print(2 + 2)

#print('Jose ' + 12) ----> Error
print('Jose ' + '12')

#Transform from number to string
age = 12 
print('Mi edad es ' + str(age))

print(f'Mi edad es {age}')

#Transform from string to number
age = input('Escribe tu edad => ')
print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 años sera {age + 10}')


name: str = 'Name'

age: int = 10