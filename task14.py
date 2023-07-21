n = int (input ('Введите число: '))
i = 0
stepen_2 = 1
while stepen_2 <= n:
    print (stepen_2, end=' ')
    i += 1
    stepen_2 = 2 ** i
