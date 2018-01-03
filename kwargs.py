#coding=utf-8

print '使用kwargs定义一个字典初始化函数'
def dict_init(**kwargs):
    return kwargs
print '初始化一个字典', dict_init(a=1, b=2, c='3')

