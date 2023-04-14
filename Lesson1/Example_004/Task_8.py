
print("Последовательно введите три числа: ")
a, b, c = int(input()), int(input()), int(input())

if c % a == 0 or c % b == 0:
    print("yes")
else:
    print("no")    