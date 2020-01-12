# Best place to change this env variables is project/settings/local_env.py file. It loads after this one specially to
# allow you manage env without touching project code.

from decouple import config
DEBUG = config('DEBUG', cast=bool)
PRODUCTION = not DEBUG
