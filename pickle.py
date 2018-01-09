# coding=utf-8
import os

try:
    import cPickle as pickle
except ImportError:
    import pickle

import json


print '# python序列化/反序列化'

d = None
path = './dumps/pickle_test.txt'
if os.path.exists(path):
    with open(path, 'rb') as f:
        d = pickle.load(f)
else:
    d = dict(name='Bob', age=20, score=88)
d['age'] = d['age'] + 1

with open(path, 'wb') as f:
    pickle.dump(d, f)

with open(path, 'rb') as f:
    print pickle.load(f)


print '# json序列化/反序列化'


json_path = './dumps/json_text.json'
d1 = None
if os.path.exists(json_path):
    with open(json_path, 'rb') as f:
        d1 = json.load(f)
else:
    d1 = dict(name='Tony', age=18)

d1['age'] = d1['age'] + 2

with open(json_path, 'wb') as f:
    json.dump(d1, f)

with open(json_path, 'rb') as f:
    print json.load(f)

print '## json序列化对象'


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


json_str = json.dumps(Student('tac', 18, 92), default=lambda obj: obj.__dict__)

print(json_str)


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print json.loads(json_str, object_hook=dict2student)