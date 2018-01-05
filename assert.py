# coding=utf-8
import logging
logging.basicConfig(level=logging.DEBUG)


def foo(s):
    try:
        n = int(s)
        assert n != 0, 'n is zero!'
        return 10 / n
    except AssertionError as e:
        print e


foo('0')


def foo1(s):
    logging.info('开始执行foo1')
    logging.debug('将"%s"转换为int类型' % s)
    n = int(s)
    logging.debug('转换后的值%d' % n)
    if(n == 0):
        logging.error('输入值不能为0，将返回None')
    else:
        logging.info('执行顺利完成')
        return 10 / n


foo1('0')
foo1('1')

