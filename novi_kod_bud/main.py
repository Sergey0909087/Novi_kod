# from random import randint as rint, choice as ch
# from math import pi
# print(rint(1, 10))
# print(pi)

# __all__ = ['func', 'MyClass']

# number = 35

# def func():
#     print("hello")

# func()

# class MyClass:
#     pass

# import random

# a = [1, 2, 3, 4]

# index = random.randint(0, len(a)-1)
# rand_num = a[index]
# print(rand_num)

# print(random.choice(a))

# import test

# def func_b():
#     main.func_b()

# class Base:
#     pass

from calc import add, sub, mul, div

class Calcul:
    def __init__(self) -> None:
        self.main()
    def main(self):
        print('Это калькулятор')
        while True:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
            choice = int(input("выбирите необходимое действие 1: +, 2: -, 3: *, 4: /, 0: Выход\n"))
            match choice:
                case 0:
                    print("Для завершения нажми на enter")
                    input()
                    break
                case 1:
                    print(add(num1, num2))
                case 2:
                    print(sub(num1, num2))
                case 3:
                    print(mul(num1, num2))
                case 4:
                    if num2 == 0:
                        print("на ноль нельзя делить")
                    else:
                        print(div(num1, num2))
                case _:
                    print('Неверный выбор')
obj = Calcul()

