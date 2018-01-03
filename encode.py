#coding=utf-8
print
print ord('A')
print chr(65)


# 使用unicode编码
print '## 编码测试'
print '\'中文\' unicode length:', len(u'中文')
print '\'ABC\' unicode length：', len(u'ABC')

print '\'中文\' utf-8 length：', len(u'中文'.encode('utf-8'))
print '\'ABC\' utf-8 length：', len(u'ABC'.encode('utf-8'))

# 以下两行代码需要在交互模式下单独执行才能看到效果
# u'中文'
# u'中文'.encode('utf-8')

print '## 解码测试'
string = '\xe4\xb8\xad\xe6\x96\x87'
string_origin = r'\xe4\xb8\xad\xe6\x96\x87'
print string_origin, '解码后：' , string.decode('utf-8')


print '##　格式化'
print 'hello %s' % 'world'
print 'i have %d dollar, maybe say %0.2f dollar' % (1.0, 1.0)


