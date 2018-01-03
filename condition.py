#coding=utf-8
# condition

print
c1 = True
if c1:
	print 'hello'

c1 = not c1
if not c1:
	print 'welcome'

print
print '非bool值条件判断'
if 'str':
	print '\'str\' is true'
if not '':
	print '\'\' is false'
if '  ':
	print '\'   \' is true'
if 1:
	print '1 is true'
if not 0:
	print '0 is false'
if -1:
	print '-1 is true'
if [1]:
	print '[1] is true'
if not []:
	print '[] is false'




