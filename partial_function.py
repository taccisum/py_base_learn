#coding=utf-8

import functools

print '使用functools定义一个将二进制表示的字符串转换为int的函数'
int2 = functools.partial(int, base=2)
print int2('101101')

print
max2 = functools.partial(max, 10, 20)
print max2(15, 17, 2, 5)
print max2(21, 17, 2, 5)