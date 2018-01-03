#coding=utf-8

ls = [1, 2, 3, 4, 5, 6, 7]
print '定义一个list', ls

print

print '取前三个元素', ls[0:3]
print '取第二、第三及第四个元素', ls[1:4]

print
print '取倒数第二、第三个元素', ls[-3:-1]
print '取最后两个元素', ls[-2:]

print
print '前5个数中，每隔一个数取一个', ls[0:5:2]
print '所有数，每隔一个数取一个', ls[::2]

print
print '复制一个list', ls[:]

print
print '###################'
print
tp = (1, 2, 3, 4, 5, 6, 7, 8)
print '定义一个tuple', tp

print
print 'tuple也可以执行切片，但结果仍为tuple', tp[0:3]

