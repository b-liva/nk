from .base import *

SECRET_KEY = os.environ['SECRET_KEY_TEST']
TEST_RUNNER = "django.test.runner.DiscoverRunner"
DB_DRIVER = os.environ.get('DB_DRIVER', 'sqlite')

if DB_DRIVER == 'mysql':

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME', 'nk_test'),
            'USER': os.environ.get('DB_USER', 'root'),
            'PASSWORD': os.environ.get('DB_PASS', ''),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'TEST': {
                'NAME': os.environ.get('DB_NAME_TEST', 'testdb'),
                'CHARSET': 'utf8',
                'COLLATION': 'utf8_general_ci',
            },
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                # 'init_command': 'ALTER DATABASE <YOUR_DB_NAME> CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci',
            },
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(ROOT_DIR, 'test_db.sqlite3'),
        }
    }
print(DATABASES)
