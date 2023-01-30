months = {
        1: 'Январе',
        2: 'Феврале',
        3: 'Марте',
        4: 'Апреле',
        5: 'Мае',
        6: 'Июне',
        7: 'Июле',
        8: 'Августе',
        9: 'Сентябре',
        10: 'Октябре',
        11: 'Ноябре',
        12: 'Декабре'
    }


number_of_month = int(input())
if not number_of_month >= 1 and number_of_month <= 12:
    print('Требуется ввести реальный номер месяца')
else:
    if number_of_month >= 3 and number_of_month <= 5:
        print(f"Вы родились в {months[number_of_month]}. Птицы пели прекрасные песни")
        """
        print('Вы родились в ' + months[number_of_month] + '. Птицы пели прекрасные песни')
        """

    elif number_of_month >= 6 and number_of_month <= 8:
        print('Вы родились в ' + months[number_of_month] + '. Солнце светило ярче чем когда-либо')
    elif number_of_month >= 9 and number_of_month <= 11:
        print('Вы родились в ' + months[number_of_month] + '. Урожай был невероятным')
    else:
        print('Вы родились в ' + months[number_of_month] + '. За окном падал белый снег')