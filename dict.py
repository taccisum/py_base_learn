#coding=utf-8
# dict.py

print

print '## dict简单运用'
_dict = {'tac': 18, 'dd':17, 'anit': 17}
print _dict
print _dict['tac']
print _dict['dd']

# 下面这行代码会报错
# print _dict['hhh']
# 可以这样写
print _dict.get('hhh')
print _dict.get('hhh', 23)

print '删除一个键值对'
_dict.pop('anit')
print _dict


