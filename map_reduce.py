#coding=utf-8

print '# map'

def _pow(num):
    return num * num;
print 'map[1-10]，获取每个元素自身平方运算的结果', map(_pow, range(1, 11))
print 'map[1-10]，将每个元素转换为字符串', map(str, range(1, 11))
def _capitalize(s):
    return s.capitalize()
ls0 = ['anit', 'tac', 'cisum']
print 'map%s，将每个元素首字母转换为大写 %s' % (ls0, map(_capitalize, ls0))

print
print '# reduce'
def _sum(result, element):
    return result + element
print 'reduce[1-100]求和', reduce(_sum, range(1, 101))

ls1 = [1, 3, 5, 6, 8, 13]
def str_and_join(result, element):
    return str(result) + str(element)
print 'reduce%s，将每个元素转换为字符串并拼接 %s' % (ls1, reduce(str_and_join, ls1))

def _prod(result, element):
    return result * element
print 'reduce[1-10]求积', reduce(_prod, range(1, 10))

