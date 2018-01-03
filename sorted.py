#coding=utf-8

ls = [1, 7, 4, 21, 3, 14]
print '排序%s -> %s' % (ls, sorted(ls))

def reversely_cmp(x1, x2):
    if x1 > x2:
        return -1
    elif x1 < x2:
        return 1
    else:
        return 0
print '反向排序%s -> %s' % (ls, sorted(ls, reversely_cmp))


