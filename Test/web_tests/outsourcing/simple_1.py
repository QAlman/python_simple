# Нужно написать функцию, которая на вход принимает две строки, и выдаёт
# список слов из первой строки, префиксом которых является вторая строка
# Например
# Вход: "ab abc def abc xyz ace ab", "ab"
# Выход: ["ab", "abc", "abc", "ab"]


a = "ab abc def abc xyz ace ab"
c = "ab"
b = ["ab", "abc", "abc", "ab"]

# # str.startswith(prefix) -> bool
# d = a.split(" ")
# def sample(d, c):
#     for i in d
#     if d[:ab]:
#         print

# #         ----------------
# Признаки
# активного
# окна:
#
#
# class ="event"  - одинаковый для всех активных окон
#
#
# title = "Работник №1" - может
# быть
# одинаковым
# либо
# уникальным
# для
# активных
# окон
#
# data - id = "9790602125" - всегда
# уникальный
# для
# активного
# окна
#
#
# class ='button' -  уникальный для кнопки "Удалить"
#
#
# --------------
#
# Написать
# решение
# которое
# позволяет
# последовательно
# удалить
# все
# активные
# окна, при
# их
# наличии
# активных
# окон
# может
# быть <= 36
#
# используя - paython and selenium
# ----------------

##########
x = 10
def foobar():
    global x
    print(x)
    x += 1
foobar()




score = 91

def score2mark(score):

        if 0 <= score <= 59:
            print(2)
            return 2
        elif 60 <= score <= 74:
            print(3)
            return 3
        elif 75 <= score <= 89:
            print(4)
            return 4

        elif 90 <= score <= 100:
            print(5)
            return 5


        assert score <= 90 and score <= 100, "Score Не корректен"
        assert score > 100, "Score Не корректен"
        assert score < 0, "Score Не корректен"

        raise ValueError("Invalid score %s" % score)


score2mark(score=0)



