import student_info as sti
import cabinet_info as cbi

print()

def menu():
    print('ГЛАВНОЕ МЕНЮ')
    print('Вас приветствует программа с данными об обучении студентов')
    mi = int(input('\n \
    1.Поиск ID студента по фамилии: \n \
    2. Посмотреть класс и место которое занимает студент \n \
    3.Выход\n \
    Вашь выбор: '))
        
    if mi == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in sti.study_card['Фамилия']:
            index = sti.study_card['Фамилия'].index(Surn)
        print(f"{sti.study_card['ID'][index]}, {sti.study_card['Имя'][index]},{sti.study_card['Фамилия'][index]}\n,{sti.study_card['Дата рождения'][index]}, {sti.study_card['Успеваемость'][index]}")
        print('\nВернуться в главное меню? 1 для продолжения 0 для выхода: ')
        num = int(input())
        if num == 1:
            menu()
        else:
            exit()

    elif mi == 2:
        c = input('Введите ID студента для вывода по классам: ')
        if c in cbi.class_card['ID']:
            index = cbi.class_card['ID'].index(c)
            print(f" Сидит в классе - {cbi.class_card['Предмет'][index]}\n, за партой номер - {cbi.class_card['№ парты'][index]}, это {cbi.class_card['Ряд'][index]}, парта - {cbi.class_card['Вид парты'][index]}, Имя: {sti.study_card['Имя'][index]}, Фамилия - {sti.study_card['Фамилия'][index]}, и успеваемасть у студента: {sti.study_card['Успеваемость'][index]}")
            print('\nВернуться в главное меню? 1: для продолжения 0: для выхода: ')
            num = int(input())
            if num == 1:
                menu()
            else:
                exit()
    else:
        print('Пока')
    exit()


menu()