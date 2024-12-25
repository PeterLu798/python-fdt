# 类的定义
class Hero(object):
    name = "Hero"  # 属性

    def info(self):  # self表示实例本身（相当于Java的this？）
        print("I am the class Hero")


# 创建对象
hero = Hero()
print(hero.name)  # Hero
hero.info()  # I am the class Hero


class Student():
    name = "Peter"

    def info(self):
        print("xxx")


print(Student.__dict__)  # 查看类的属性
print(Student.__dict__["name"])  # 查看单个属性
print(Student.name)  # 查看属性
Student.age = 18  # 新增属性
Student.name = "Lucy"  # 修改属性
del Student.age  # 删除属性


class Order:
    def __init__(self, id, costprice, sellprice):
        self.id = id
        self.costprice = costprice
        self.sellprice = sellprice

    def getprofit(self):
        return self.sellprice - self.costprice


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name}被销毁了")


person = Person("kk")

del person

order = Order(1, 32.1, 68.2)
print(f"订单 {order.id} 的利润是{order.getprofit()}")


class A:
    _name = "LL"
    __age = 18  # 私有属性

    def get_age(self):
        return self.__age

    def set_sex(self, sex):
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    def __printfoo(self):  # 私有方法
        print("foo")

    def printsth(self):
        self.__printfoo()  # 调用私有方法
        print("sth.")


a = A()
print(A._name)  # LL
# print(A.__age)  # AttributeError: type object 'A' has no attribute '__age'. Did you mean: '_A__age'?
print(a._name)  # LL
# print(a.__age)  # AttributeError: 'A' object has no attribute '__age'. Did you mean: '_A__age'?
print(a.get_age())  # 正确访问私有属性的方式
a.printsth()
a.set_sex("男")
print(a.get_sex())


class A1:
    def printa1(self):
        print("a1")


class B(A, A1):
    pass  # 什么都不写


b = B()
b.printsth()
b.printa1()


class C:
    def printc(self):
        print("c")


class C1(C):

    def printc1(self):
        print("c1")


class C2(C1):
    pass


c2 = C2()
c2.printc()
c2.printc1()


class Animal:
    def say(self):
        print("")

    def eat(self):
        print("Eat meat")


class Dog(Animal):
    def say(self):
        print("Wangwang")

    def eat(self):
        super().eat()
        print("Eat noodle")


dog = Dog()
dog.say()
dog.eat()
