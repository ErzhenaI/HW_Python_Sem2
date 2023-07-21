s = int (input ("Сумма натуральных чисел в диапазоне <=1000 равна: "))
p = int (input ("Произведение натуральных чисел в диапазоне <=1000 равно: "))
for x in range (s):
    for y in range (p):
        if (x + y) == s and (x * y) == p:
            first_n = x
            second_n = y
print (f'Первое число равно {first_n}. Второе число равно {second_n}')
