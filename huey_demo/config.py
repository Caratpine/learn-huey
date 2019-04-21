# coding=utf-8

from huey import RedisHuey

huey = RedisHuey('huey_demo', host='localhost', password='just4redis')
