name = 'Jose'
last_name = 'Nunez'
print(name)
print(last_name)
full_name = name + ' ' + last_name
print(full_name)
print(f'this is my {full_name}')

quote = 'I"m Jose'
print(quote)
quote2 = "I'm Jose David"
print(quote2)

#format 
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1',template)

template2 = 'Hola mi nombre es {} y mi apellido es {}'.format(name, last_name)
print('v2',template2)

template3 = f'Hola mi nombre es {name} y mi apellido es {last_name}'
print('v3', template3)
