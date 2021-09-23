"""
https://stepik.org/lesson/534343/step/4?unit=527467
Задание: проверка знаний — 2
В задаче ниже используются темы:

списки;
циклы;
строки;
условия;
функции.
Условие задачи:
Напишите функцию с названием detect_lucky, которая принимает в качестве аргумента шестизначное число и возвращает True, если оно является счастливым, и False в противном случае. Счастливым называется шестизначное число, сумма первых трех цифр которого равна сумме последних трех цифр.

Например, число 237831 является счастливым: 2+3+7 = 12 и 8+3+1 = 12. А 12 =12, поэтому функция вернет True.

Вызов функции уже прописан. Вам остается написать только саму функцию.

Примечание. Код должен возвращать значение, а не печатать его на экран.

Sample Input:

985778
Sample Output:

True
"""
import random


def detect_lucky(number):
    number = str(number)
    left = int(number[0]) + int(number[1]) + int(number[2])
    right = int(number[3]) + int(number[4]) + int(number[5])
    return left == right


def _text_lucky():
    for i in range(10):
        number = round(random.random()*899999 + 100000)
        print(number, detect_lucky(number))


_text_lucky()
