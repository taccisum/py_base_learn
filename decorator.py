#coding=utf-8

print '# 简单的装饰器'
print '定义一个简单的装饰器'
def log(func):
    def wrapper(*args, **kw):
        print 'call %s(), args: %s' % (func.__name__, args)
        return func(*args, **kw)
    return wrapper

# 相当于定义了my_func=log(my_func)
print '使用装饰器装饰my_func()'
@log
def my_func(name):
    print 'hello world, my name is %s' % (name)

print '调用my_func()'
my_func('tac')
print 'my_func.__name__:', my_func.__name__


print
print '# 带参数的装饰器'
print '定义一个带参数的装饰器'
def log_with_args(text):
    def inner_decorator(func):
        def wrapper(  *args, **kw):
            print '%s %s(), args: %s' % (text, func.__name__, args)
            return func(*args, **kw)
        return wrapper
    return inner_decorator
print '使用带参数的装饰器装饰my_func1()'
# 相当于定义了my_func1=log('execute')(my_func)
@log_with_args('execute')
def my_func1(name):
    print 'hello world, my name is %s' % (name)
my_func1('tac')
print 'my_func1.__name__:', my_func1.__name__

