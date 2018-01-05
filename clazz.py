# coding=utf-8

print '# 简单类定义'


class Student(object):  # 从object继承
    id_count = 1

    def __init__(self, name, score):    # 构造函数，self表示实例本身
        self.__name = name  # 私有变量，无法访问
        self.score = score  # 公开变量，可以访问
        self.__id__ = Student.id_count  # 特殊变量，可以访问
        Student.id_count = Student.id_count + 1

    def print_score(self):  # 类中定义的方法，第一个参数永远是self（但调用的时候无需传这个参数）
        print '%s: %s' % (self.__name, self.score)


print Student('', 1)
print Student

Student('tac', 119).print_score()
Student('anit', 118).print_score()
stu = Student('cisum', 111)
# print stu.__name  # 无法从外部访问_name，这行代码执行会报错
print stu.score
print stu.__id__


print
print '#　类继承'


class Animal(object):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print self.name


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__('dog')


class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__('cat')

    def print_name(self):
        super(Cat, self).print_name()
        print 'hh'


Dog().print_name()
Cat().print_name()


print '# 获取对象信息'

print type(123)
print type('123')
print type(abs)
print type(Dog)
print type(Dog())

print
import types

print types.ListType
print types.StringType
print types.TypeType


print
print '获取属性和方法'
print 'list的属性和方法：', dir([])
print 'str的public方法', [e for e in dir('asd') if not e.startswith('_')]
print 'int的public方法', filter(lambda e : not e.startswith('_') , dir(123))


print
print '获取长度'
print len('abc')
print 'abc'.__len__() # 等价

class FooObj(object):
    def __len__(self):
        return 10
print len(FooObj())

print
print '操作对象属性或方法'
class Foo1Obj(object):
    def __init__(self):
        self.name = ''
        self.__name = ''
        self.__name__ = ''

    def dosomething(self):
        pass

print hasattr(Foo1Obj(), 'name')
print hasattr(Foo1Obj(), '__name')
print hasattr(Foo1Obj(), '__name__')
print hasattr(Foo1Obj(), 'dosomething')
foo = Foo1Obj()
setattr(foo, 'name', 'hhh')
print getattr(foo, 'name')
print getattr(foo, 'name1', 'default')




