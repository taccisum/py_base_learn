# coding=utf-8

print '# 过滤器'


def is_even(num):
    return num % 2 == 0


print '只保留[1-20]中的偶数 %s' % filter(is_even, range(1, 21))

ls = ['anit', '', None, '  ', ' tac']


def not_empty(s):
    return s is not None and s.strip() is not ''


print '过滤掉%s中的空字符串 %s' % (ls, filter(not_empty, ls))

