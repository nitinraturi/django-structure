AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#Third Party Apps
INSTALLED_APPS += [

]

#Custom Apps
INSTALLED_APPS += [
    'apps.users',
    'apps.pages',
]
