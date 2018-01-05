# coding=utf-8
import os

print '获取操作系统名字', os.name   # posix表示*nix系统，ut表示windows系统
print '获取系统的详细信息', os.uname()
print '获取环境变量', os.environ
print '获取指定环境变量', os.getenv('HOME')

print '查看当前目录绝对路径', os.path.abspath('.')
tmp_path = os.path.join('.', 'asset', 'tmp')
print '拼接路径', tmp_path
print '创建目录'
if not os.path.exists(tmp_path):
    os.mkdir(tmp_path)
    print '创建成功'
else:
    print '目录已存在，将不会重新创建'

print '删除目录'
assert os.path.exists(tmp_path)
os.rmdir(tmp_path)
print '删除成功'

print
path = './asset/tmp/123.txt'
print '拆分路径%s -> %s' % (path, os.path.split(path))
print '拆分扩展名%s -> %s' % (path, os.path.splitext(path))





