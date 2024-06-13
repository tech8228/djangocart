import os
from .common import *


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['cart-prod-b4918a8c7020.herokuapp.com']