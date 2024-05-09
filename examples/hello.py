import helper
from myabc import Rectangle
from my_dec import around_decorator

import routes

@around_decorator
def greeting():
    print("greetings")

def greet(name):
    print("hello, ",name)

def main():
    print("Hello, World!")
    print(helper.print_message(12,45.55))
    r=Rectangle(5,4)
    print(r.area())
    print(r.perimeter())
    greet("123")
    print(routes.mod_name())
# 调用主函数
if __name__ == "__main__":
    main()
