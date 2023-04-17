
import random
from random import randint

total_coins = int(input("Введите количество монет: "))

a = 0
b = 0

coins = [0, 1]
for i in range(total_coins):
    x = random.shuffle(coins)
    print(f"Все монеты: {coins}")
    if int(coins[0]) == 0:
         b += 1
    if int(coins[0]) == 1:
         a += 1

print(f"Всего монет: {a, b}")   

if a > b:
    print(f"Минимальное количество монет, которые надо перевернуть {b}")
else:
    print(f"Минимальное количество монет, которые надо перевернуть {a}")
