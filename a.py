#这是a.py
from functools import wraps
def warrper(func):
    @wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner
@warrper
def aaa():
    pass
print(aaa.__name__)