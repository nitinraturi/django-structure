# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
import os

LANGUAGE_CODE = 'en'

USE_I18N = True
USE_L10N = True

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)
