#coding=utf-8
from collections import Iterable

print '# 最简单的生成器'
g = (x for x in range(1, 5))
print '定义一个最简单的生成器：', g
print '生成器也是一个可迭代对象，instance of Iterable: ', isinstance(g, Iterable)
print '进行迭代'
for item in g:
    print item,
print

print
print '# 使用函数作为生成算法'
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
g1 = fib(6)
print '使用函数的方式生成一个生成器fib(6): %s' % g1
print '进行迭代'
for item in g1:
    print item,
print

print
print ''
