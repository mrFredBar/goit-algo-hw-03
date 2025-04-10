from datetime import datetime

#Для себя/ вывести первое значение времени для дальнейшего использования с сравнением введенного времени
now = datetime.now()
now_str = now.strftime("%d-%m-%y ")
print('время сейчас:', now_str) 

#Ввод даты для последующего сравнения с текущей датой
date = input('введите дату в формате дд-мм-гг: ')

#Сделать функцию с ввденной датой и последуйщим сравнением с текущей датой и выводом разницы в днях
def get_days_from_today(date):
    date = datetime.strptime(date, "%d-%m-%y")
    now = datetime.now()
    delta = now - date
    return delta.days

print('разница в днях:', get_days_from_today(date))
