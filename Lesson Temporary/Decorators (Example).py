# import time
#
#
# def stopwatch(func):
#     def wrap():
#         start = time.time()
#         func()
#         finish = time.time()
#         time_to_func_exec = finish - start
#         print(f"Время выполнения составило: {round(time_to_func_exec, 2)} секунд")
#
#     return wrap()
#
#
# @stopwatch
# def hello():
#     input("Скажи Привет:")


def inspector(func):
    list_arg = []

    def wrap(arg):
        if arg in list_arg:
            print("Повторяетесь)))")
        else:
            list_arg.append(arg)
            func(arg)

    return wrap


@inspector
def hello(name):
    print(f"Привет {name}")


hello("Вася")
hello("Петя")
hello("Вася")
hello("Саша")
hello("Петя")
hello("Вася")
