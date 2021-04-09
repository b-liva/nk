from .base import *

ROOT_PATH_LOCAL = os.environ.get('ROOT_PATH', None)
if ROOT_PATH_LOCAL:
    sys.path.insert(0, ROOT_PATH_LOCAL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'nk_local'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASS', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}