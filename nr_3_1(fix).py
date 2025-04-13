from datetime import datetime

#Для себя/ вывести первое значение времени для дальнейшего использования с сравнением введенного времени
now = datetime.now()
now_str = now.strftime("%Y-%m-%d")
print('время сейчас:', now_str) 

#Ввод даты для последующего сравнения с текущей датой
date = input('введите дату в формате ГГ-ММ-ДД: ')

#Сделать функцию с ввденной датой и последуйщим сравнением с текущей датой и выводом разницы в днях
def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        now = datetime.now().date()
        delta = now - date
        return delta.days
    except ValueError:
        print('Неверный формат даты. Пожалуйста собладайте формат ГГ-ММ-ДД в следующий раз :)')
        return None


result = get_days_from_today(date)
if result is not None:
   print('разница в днях:', result)
