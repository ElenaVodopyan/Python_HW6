import random
numbers = [random.randint(0, 9) for _ in range (15)]
print(numbers)
n = int(input('Задайте число N: '))
result = ''
for el in numbers:
    result += str(el)
print(result)
if str(n) in result:
    print('есть число')
else:
    print('нет числа')