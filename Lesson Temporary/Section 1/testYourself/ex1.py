"""
https://stepik.org/lesson/534343/step/3?unit=527467
Задание: проверка знаний - 1
В задаче ниже используются темы:

списки;
циклы;
строки;
условия.
Условие задачи:
Введите с клавиатуры список с различными значениями (цифры, слова, символы). Необходимо проверить,
есть ли в этом списке два слова подряд и вывести их на экран. Если таких пар нет, то выведите фразу “Мало слов!”.

Sample Input:

Привет пока 12 когда 11 что где
Sample Output:

Привет пока
что где
"""


def solution():
    input_items = input().split()
    is_few_words = True
    for i in range(len(input_items) - 1):
        if input_items[i].isalpha():
            if input_items[i+1].isalpha():
                is_few_words = False
                print(input_items[i], input_items[i+1])
    if is_few_words:
        print('Мало слов!')


solution()
