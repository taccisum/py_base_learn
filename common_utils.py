#coding=utf-8


print '# hash库'
import hashlib

print 'md5加密'
md5 = hashlib.md5()
md5.update('123456')
print md5.hexdigest()

print 'sha1加密'
sha1 = hashlib.sha1()
sha1.update('123456')
print sha1.hexdigest()




