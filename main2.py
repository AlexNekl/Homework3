# Задание № 1:
# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# +
# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.


# numbers = {'zero': 'ноль',
#                'one': 'один',
#                'two': 'два',
#                'Three': 'три',
#                'four': 'четыре',
#                'five': 'пять',
#                'Six': 'шесть',
#                'seven': 'семь',
#                'eight': 'восемь',
#                'nine': 'девять',
#                'ten': 'десять'}
#
# def num_translate_adv(num):
#     for key, val in num.items():
#         if key[0] == key[0].capitalize():
#             print(f'{key} --> {val.capitalize()}')
#         else:
#             print(f'{key} --> {val}')
# print(num_translate_adv(numbers))

# Задание № 2:
# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

# name_list = {'Иван', 'Мария', 'Федор', 'Марина', 'Игорь', 'Феодосия'}

# def thesaurus(*names):
#     result = {}
#     for name in names:
#         key = name[0].capitalize()
#         if key not in result:
#             result[key] = []
#         result[key].append(name)
#     return result
#
# print(thesaurus('Иван', 'Мария', 'Федор', 'Марина', 'Игорь', 'Феодосия'))


# Задание № 3: Реализовать функцию get_jokes(),
# возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):


# import random
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#
#
# def get_jokes(n=3, bool=True):
#     jokes = []
#     for i in range(n):
#         jokes1 = []
#         n1 = random.choice(nouns)
#         n2 = random.choice(adverbs)
#         n3 = random.choice(adjectives)
#         jokes1.append(n1)
#         jokes1.append(n2)
#         jokes1.append(n3)
#         jokes.append(' '.join(jokes1))
#     print(jokes)
#     if bool == False:
#         jokes1.remove(n1, n2, n3)
#
# get_jokes()
