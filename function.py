#coding=utf-8

print '定义一个函数add'
def add(a,b):
	return a+b;
print '执行add(1, 2), 结果为%d' % add(1, 2)

print '定义一个返回值为None的函数returnNone'
def returnNone():
	return
print '执行结果为', returnNone()

print '执行一个直接pass的函数nop'
def nop():
	pass
print '执行结果为', nop()

print '定义一个有多个返回值的函数multi_result'
def multi_result():
	return 1, 2
a, b = multi_result()
print '执行结果为，a: %d, b: %d' % (a, b)
print '函数实际返回值是一个tuple', multi_result()


