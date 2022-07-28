try:
    tikets = int(input("Введите необходимое количество билетов:"))
    price = 0
    print()

    for i in range(1, tikets+1):
        age = int(input('Введите возраст посетителя:'))
        if age < 18:
            price = price
        if 18 <= age <= 25:
            price += 990
        if age > 25:
            price += 1390
        if age < 0 or age > 120:
            raise EnvironmentError ()

except EnvironmentError as e:
    print('Ошибка! Вам не может быть столько лет.')
except ValueError as e:
    print('Ошибка! Необходимо ввести целое число.')
else:
    print()

    if tikets > 3:
        price -= price * 0.1
        print('Сумма к оплате с учётом скидки:',int(price), 'руб.')
    else:
        print('Сумма к оплате:',price, 'руб.')






