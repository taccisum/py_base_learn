#coding=utf-8

def lazy_add():
    def add(a, b):
        return a + b
    return add

print lazy_add()(1, 2)

def lazy_add_alter(arg0, arg1):
    def add():
        return arg0 + arg1
    return add
print lazy_add_alter(2,3)()



