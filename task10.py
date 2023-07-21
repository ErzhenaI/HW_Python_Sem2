import random
count_coins = int (input ("Введите количество монет: "))
print (f'Перед нами {count_coins} монет:')
coins = [random.randint(0 ,1) for _ in range (count_coins)]
print (coins)
count, reshka = 0, 0
print ("0 - ЭТО РЕШКА, 1 - ЭТО ОРЕЛ")
for i in coins:
    if i == 0:
        count += 1
        reshka = count
print (f'Видим {reshka} решек и {count_coins - reshka} орлов в {count_coins} монетах')
if reshka < count_coins - reshka:
    print (f'\nПереверните {reshka} решек')
else:
    if reshka == count_coins // 2:
        print (f'\nПереверните {reshka} решек или {count_coins - reshka} орлов')
    else:
        print (f'\nПереверните {count_coins - reshka} орлов')
print()
