#coding=utf-8
# higher order function

print '定义一个高阶函数add(a, b, handler)'
def add(a, b, handler):
    return handler(a) + handler(b)

print '定义一个handler，对原数值作平方运算'
def _pow(num):
    return num * num;

print '执行高阶函数add(1, 3, handler)，结果%d ' % add(1, 3, _pow)
