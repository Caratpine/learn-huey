# coding=utf-8

from config import huey


@huey.task()
def count_beans(num):
    print('-- counted %s beans --' % num)
    return 'Count %s beans' % num


@huey.task(retries=3, retry_delay=10)
def try_thrice():
    print('tring...')
    raise Exception('nope')


@huey.task()
def add(a, b):
    return a + b
