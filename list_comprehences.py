#coding=utf-8
import os

print '# 生成一个[0-10]的list', range(0, 11)
print '# 生成[0-10]的数的平方的结果构成的list', [x * x for x in range(0, 11)]
print '# 生成[0-10]的数中的偶数的平方的结果构成的list', [x * x for x in range(0, 11) if x % 2 == 0]
print r'# 列出当前目录下的所有不以".py"结尾的文件/文件夹', [d for d in os.listdir('.') if not d.endswith('.py')]
