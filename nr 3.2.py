#nr 3.2
import random

#Написать функцию 'get_numbers_ticket(min, max, quantity)' которая будет генерировать набор уникальных чисел для лотереи
def get_numbers_ticket(min, max, quantity):
    
    numbers = []
    #Проверка значений 
    if quantity <=0:
       #print ('Количество чисел должно быть больше 0')
       return[]
       
    if min < 1 :
       #print('Минимальное число не выполняет требование "не меньше 1"')
       return[]
    
    if max > 1000:
       #print('Максимальное число не выполняет требование "не больше 1000"')
       return[]

    if min >= max:
       #print ('Минималное число не может быть больше или равно максимальному')
       return[]

    if quantity > (max - min + 1):
       #print ('Ошибка ввода данных. Количество чисел больше диапазона')
       return[]
    

    while len(numbers) < quantity:
        num = random.randint(min, max)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

#Ввод данных
try:
   quantity_int = int(input("Введите количество чисел в лотерее: "))
   min_int = int(input("Введите минимальное число лотереи, не меньше 1: "))
   max_int = int(input("Введите максимальное число лотереи, не больше 1000: "))

#Проверка ввода данных на отрицательные значения (просьба правки после сдачи)
   if quantity_int < 0 or min_int < 0 or max_int < 0:
      #print ('Ошибка ввода данных, введите ТОЛЬКО положительные числа')
      results = []
   else:
       results = get_numbers_ticket(min_int, max_int, quantity_int)
except ValueError:
   results = []

#Вывод результата
print ('Результаты лотереи:', results)
