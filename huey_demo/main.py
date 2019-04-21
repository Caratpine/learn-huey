# coding=utf-8

from config import huey
from tasks import count_beans, try_thrice, add  # noqa


if __name__ == '__main__':
    beans = input('How many beans\n')
    count_beans(int(beans))
    print('Enqueued job to count %s beans' % beans)
