# coding=utf-8

import re

print '使用正则表达式匹配字符串'
if re.match(r'^asd.*hjk', 'asdfghjkl'):
    print 'ok'
else:
    print 'failed'

print '使用正则表达式切割字符串'
print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,\;]+', 'a,b;; c  d')


