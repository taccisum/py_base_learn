#coding=utf-8
# loop.py

print

print '## foreach'
foos = ['bar1', 'bar2', 'bar3']
for foo in foos:
	print foo

print '## range'
print range(1,20)
s=''
for i in range(1,10):
	s = s + str(i)
print s

print '## while'
_sum = 0
n = 0
while n < 100:
	n = n + 1
	_sum += n
print _sum
