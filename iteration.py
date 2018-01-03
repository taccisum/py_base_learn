#coding=utf-8
from collections import Iterable

_dict = {'foo1': 'bar1', 'foo2': 'bar2', 'foo3': 'bar3'}
print '# 迭代一个dict', _dict

print '## 迭代key'
for key in _dict:
    print 'key: %s' % key

print '## 迭代key和value'
for key, val in _dict.iteritems():
    print 'key: %s, value: %s' % (key, val)

print
ls = [3, 4, 11]
print '# 迭代一个list', ls
for item in ls:
    print item
print '## 迭代list下标'
for index, item in enumerate(ls):
    print 'index: %d, item: %d' % (index, item)

print
_str = 'ABC'
print '# 迭代一个字符串', _str
for s in _str:
    print s

print
print '# 判断一个对象是否可以迭代'

def is_iterable(obj):
    if isinstance(obj, Iterable):
        return '可以迭代'
    else:
        return '无法迭代'

print '字符串',  is_iterable('ABC')
print '数值',  is_iterable(123)



