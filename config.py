import os
from datetime import timedelta

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SERVER_IP = '0.0.0.0'
SERVER_PORT = int(os.environ.get('PORT', 33507))

THREADS_PER_PAGE = 8
