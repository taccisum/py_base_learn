#coding=utf-8

class AirCondiction(object):
    def __enter__(self):
        print '打开空调'
        return self
    
    def __exit__(self, exctype, excvalue, traceback):
        print '关闭空调'

    def work(self, status):
        if status:
            print 'work fine'
        else:
            print 'work not fine'

if __name__  == '__main__':
    with AirCondiction() as ac:
        ac.work(True)
