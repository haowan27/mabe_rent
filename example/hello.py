import helper
from myabc import Rectangle
from my_dec import around_decorator

import routes


class Wallet:
    def __init__(self, size, money):
        self.size = size
        self.money = money


class Person:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
    def Type(self):
        return type(self)

person = Person("xiaozhang", 24,Wallet(10,20))


class Student(person.wallet):


@around_decorator
def greeting():
    print("greetings")


def greet(name):
    print("hello, ", name)


def main():
    print("Hello, World!")
    print(helper.print_message(12, 45.55))
    r = Rectangle(5, 4)
    print(r.area())
    print(r.perimeter())
    greet("123")
    print(routes.mod_name())


# 调用主函数
if __name__ == "__main__":
    main()
