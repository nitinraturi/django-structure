# Best place to change this env variables is project/settings/local_env.py file. It loads after this one specially to
# allow you manage env without touching project code.

from decouple import config
DEBUG = config('DEBUG')
PRODUCTION = not DEBUG
SECRET_KEY = config('SECRET_KEY')
