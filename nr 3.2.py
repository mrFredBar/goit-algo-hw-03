#nr 3.2
import random

quantity = int(input("Введите количество чисел в лотерее: "))
min = int(input("Введите минимальное число лотереи, не меньше 1: "))
max = int(input("Введите максимальное число лотереи, не больше 1000: "))

#Проверка значений 
if quantity <0:
    print ('Количество чисел должно быть больше 0')
if min < 1 :
    print('Минимальное число не выполняет требование "не меньше 1"')
    exit()
if max > 1000:
    print('Максимальное число не выполняет требование "не больше 1000"')
    exit()
if min >= max:
    print ('Минималное число не может быть больше или равно максимальному')
    exit()

#Написать функцию 'get_numbers_ticket(min, max, quantity)' которая будет генерировать набор уникальных чисел для лотереи
def get_numbers_ticket(min, max, quantity):
    numbers = []
    while len(numbers) < quantity:
        num = random.randint(min, max)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

#Вывод результата
print ('Результаты лотереи:', get_numbers_ticket(min, max, quantity))