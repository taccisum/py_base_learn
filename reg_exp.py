# coding=utf-8

import re

print '使用正则表达式匹配字符串'
if re.match(r'^asd.*hjk', 'asdfghjkl'):
    print 'ok'
else:
    print 'failed'

print
print '使用正则表达式切割字符串'
print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,\;]+', 'a,b;; c  d')

print
print '预编译正则表达式'
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
