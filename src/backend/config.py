import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'\x927O\x7f\xcc\xd4\xaf*\xa2\x8e\xef\x0b\xc8\xe2\x1ez'"
    MONGODB_SETTINGS = {'db':'DatabaseName'}