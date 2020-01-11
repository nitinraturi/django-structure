from decouple import config
# SERVER_EMAIL = ''
# DEFAULT_FROM_EMAIL = ''
# ADMINS = (('Your name', 'your@email.here'),)

# Email Configuration
EMAIL_USE_TLS = config('EMAIL_USE_TLS',cast=bool)
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT',cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
