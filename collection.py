#coding=utf-8
print
print '## 测试list'

ls = ['123', 456, 789.0]
print ls
print '索引为1的元素', ls[1]
print 'list长度',len(ls)

print 'append \'hello\' 到list'
ls.append('hello')
print ls

print 'insert \'?\'到索引为1的位置'
ls.insert(1, '?')
print ls

print 'pop一个元素', ls.pop()
print ls

print 'pop索引为0的元素', ls.pop(0)
print ls

print '定义空list'
empty = []
print '空list长度', len(empty)


print
print '## 测试tuple'
tp = ('123', 456, 789.0)
print tp

# 不支持诸如以下的修改
# tp[1] = …
# tp.append(…)
# tp.insert(…)

print '定义只有一个元素的tuple'
single = (12,)
print single
print '索引为0的元素', single[0]
print 'tuple长度', len(single)


