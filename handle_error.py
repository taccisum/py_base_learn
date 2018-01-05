# coding=utf-8
import logging

print '# 简单的异常捕捉'
try:
    '1' + 1
except TypeError as e:
    print '出错啦，类型错误'
    logging.exception(e)    

finally:
    print '正确结果应该是', 1 + 1


print
print '# 自定义异常'
class FooException(BaseException):
    pass

try:
    raise FooException('foo excpetion happend')
except FooException as e:
    print '出错啦'
    logging.exception(e)




