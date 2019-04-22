# coding=utf-8

from flask import Blueprint

from web.tasks import count_beans

bp = Blueprint('task', __name__)


@bp.route('/')
def index():
    res = count_beans(100)
    print(res)
    return 'hello world'
