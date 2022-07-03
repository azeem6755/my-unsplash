from my_unsplash.settings.base import *


STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_root')
STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), 'dist'),
]
DEBUG = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'