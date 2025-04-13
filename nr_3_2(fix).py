#nr 3.2
import random

#Написать функцию 'get_numbers_ticket(min, max, quantity)' которая будет генерировать набор уникальных чисел для лотереи
def get_numbers_ticket(min, max, quantity):
    
    numbers = []
    #Проверка значений 
    if quantity <=0:
       print ('Количество чисел должно быть больше 0')
       exit()
       
    if min < 1 :
       print('Минимальное число не выполняет требование "не меньше 1"')
       exit()

    if max > 1000:
       print('Максимальное число не выполняет требование "не больше 1000"')
       exit()

    if min >= max:
       print ('Минималное число не может быть больше или равно максимальному')
       exit()

    if quantity > (max - min + 1):
       print ('Ошибка ввода данных. Количество чисел больше диапазона')
       exit()

    while len(numbers) < quantity:
        num = random.randint(min, max)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

#Ввод данных
quantity_int = int(input("Введите количество чисел в лотерее: "))
min_int = int(input("Введите минимальное число лотереи, не меньше 1: "))
max_int = int(input("Введите максимальное число лотереи, не больше 1000: "))

#Вывод результата
results = get_numbers_ticket(min_int, max_int, quantity_int)
print ('Результаты лотереи:', results)