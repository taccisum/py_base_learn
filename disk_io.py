# coding=utf-8
import os

print '# 文件读操作'
try:
    f = open('./asset/greeting.txt', 'r')
    print f.read()
    print f.closed
finally:
    f.close()

print f.closed

print
print '## 使用with简化操作'
with open('./asset/greeting.txt', 'r') as f:
    print f.read()

# tip: 所有具有read方法的对象统称为file-like object，不需要从某个其它类继承

print
print '## 读取图片'
with open('./asset/Avatar1.jpg', 'rb') as f:
    print f.read(100)

print
print '# 文件写操作'
with open('./asset/tmp.txt', 'w') as f:
    f.write('hello disk io')
with open('./asset/tmp.txt', 'r') as f:
    print f.read()
    os.remove(f.name)
    



