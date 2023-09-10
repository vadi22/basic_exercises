# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import *

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
list_name =([st['first_name'] for st in students])
for name in set(list_name):
    print(f'{name}: {list_name.count(name)}')
print()


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
list_name = [st['first_name'] for st in students]
print(f'Самое частое имя среди учеников: {Counter(list_name).most_common(1)[0][0]}')
print()

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for i in range (len(school_students)):
    list_name = [st['first_name'] for st in school_students[i]]
    print(f'Самое частое имя среди учеников: {Counter(list_name).most_common(1)[0][0]}')
print()




# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for class_num in school:
    list_students = [st['first_name'] for st in class_num['students']]
    gender_students = [is_male[name] for name in list_students]
    girls, boys = gender_students.count(False), gender_students.count(True)
    print(f'Класс {class_num["class"]}: девочки {girls}, мальчики {boys}')
print()



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
max_girls =0
max_boys = 0

for class_num in school:
    list_students = [st['first_name'] for st in class_num['students']]
    gender_students = [is_male[name] for name in list_students]
    girls, boys = gender_students.count(False), gender_students.count(True)
    if girls > max_girls:
        class_girls = class_num['class']
    if boys > max_boys:
        class_boys = class_num['class']
print(f'Больше всего девочек в классе {class_girls}')
print(f'Больше всего мальчиков в классе {class_boys}')
print()


