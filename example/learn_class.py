from util.singleton import Singleton


class Person(Singleton):
    name = ""
    age = 0

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age


obj1 = Person("zhangsna", 13)
# obj2 = Person("lisi",13)

# print(obj1 is obj2)


class MyClass:
    class_attribute = "class attribute"

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print("cls =", cls)
        print("cls.class_attribute =", cls.class_attribute)

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

    def attr_has(self):
        if hasattr(self, "asdf"):
            print(True)
        else:
            print(False)

    def set_asdf(self):
        self.asdf = "123"


# MyClass.class_method()

# meclass = MyClass("in 123")
# print(meclass.instance_attribute)


# class MyClass:
#     def __new__(cls, *args, **kwargs):
#         print("__new__ method is called")
#         instance = super().__new__(cls)
#         return instance

#     def __init__(self, *args, **kwargs):
#         print("__init__ method is called")
#         print("self inside __init__:", self)

# 创建 MyClass 的实例
obj = MyClass(123)
# obj2 = MyClass()
obj.attr_has()
obj.set_asdf()
obj.attr_has()
print(id(obj))
# print("obj is obj2 : ",obj is obj2)
