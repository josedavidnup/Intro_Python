# python 17_crud.py
# CRUD
numbers = [
  1,
  2,
  3,
  4,
  5,
]

print(numbers[1])

numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'Hola')
print(numbers)

numbers.insert(3, True)
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(index)
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers1 = [1, 3, 7, 2, 5, 10, 9, 4]
numbers1.sort()
print(numbers1)

text1 = ['za', 'ra', 'al']
text1.sort()
print(text1)
