import random
import datetime
'''
1. Напишите функцию (F): на вход список имен и целое число N;
на выходе список длины N случайных имен из первого списка
(могут повторяться, можно взять значения: количество имен 20, N = 100,
рекомендуется использовать функцию random);
'''

names_list = ['Ivan', 'Alexandr', 'Dmitry', 'Anton', 'Artem', 'Julia', 'Elena', 'Natali',  'Pavel', 'Valery', 'Timur', 'Egor', 'Bulat', 'Vasily', 'Foma', 'Marat', 'Albert', 'Kirill', 'Iskander', 'Amir']
N = 100

def F(names, N):
    '''
    :param names: список имен
    :param N: длина списка
    :return: список длиной N случайных именн из списка
    '''
    emp_list = []
    for i in range(N):
        emp_list.append(random.choice(names))
    return emp_list
f_list = F(names_list, N)
print('100 имен:', f_list)

'''
2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
'''

def F(x):
    '''
    :param x: список случайных имен
    :return: словарь с именами и их количеством повторов
    '''
    my_dict = dict.fromkeys(f_list, 0)
    for i in f_list:
        my_dict[i] += 1
    return my_dict
f_dict = F(f_list)

def F(y):
    '''
    :param y: имена и их количество повторов
    :return: самое частое имя
    '''
    dict_oft = list(f_dict.items())
    dict_oft.sort(key=lambda i: i[1], reverse=True)
    return dict_oft
f2_dict = F(f_dict)
print('Самое частое имя: ', f2_dict[0][0])

'''
3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
'''

def F(z):
    '''
    :param z: список случайных имен
    :return: Редкая буква
    '''
    f3_dict = {}
    for i in z:
        for a in i:
            f3_dict[a] = f3_dict.get(a, 0) + 1
    f3_dict = sorted(list(f3_dict.items()), key=lambda x: x[1])
    return f3_dict[0]
f4_dict = F(f_list)
print('Самая редкая буква, с которой начинаеются имена: ', f4_dict)

'''
4. В файле с логами найти дату самого позднего лога (по метке времени)
'''

log_file = open('log', 'r', encoding = 'utf-8')

def F(logs):
    '''
    :param logs: файл с логами
    :return: дата позднего лога
    '''
    date = []
    log_text = log_file.read().split(sep='\n')
    data_list = [log_text[i][0:10] for i in range(len(log_text))]
    data_list.sort()
    return data_list[-1]
print('Дата самого позднего лога: ', F(log_file))
