#coding=utf-8

id_counter = 0

class FooClazz(object):
    def __init__(self):
        global id_counter
        self.id = id_counter
        id_counter = id_counter + 1

for i in range(0, 10):
    print FooClazz().id
