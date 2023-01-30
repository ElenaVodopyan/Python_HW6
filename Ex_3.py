def check_numbers(x,y):
    min_numbers = min(x,y)
    divide = 1
    for el in range(2, min_numbers+1):
        if x % el == 0 and y % el == 0:
            divide = el
            break
    return divide == 1

for y in range(1, 12):
    for x in range(1, y):
        if check_numbers(x, y):
            print(f'{x}/{y}', end = ' ')
    print()