from .base import *
from dotenv import load_dotenv
from Dante.logging import *
from corsheaders.defaults import default_headers
load_dotenv(Path.joinpath(BASE_DIR,'.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = 'RENDER' not in os.environ
DEBUG = False
ALLOWED_HOSTS = ['dinietts-c33ix.ondigitalocean.app']
DATABASES =  {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),     
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),     
        'SSLMODE' : 'require'
    }
}

STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_TRUSTED_ORIGINS = ['https://dinietts-c33ix.ondigitalocean.app','https://*.127.0.0.1']
SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True


CORS_ORIGIN_WHITELIST = [
    "https://dinietts-c33ix.ondigitalocean.app",
    # Agrega aquí otros orígenes permitidos si es necesario
]
CORS_ALLOW_ALL_ORIGINS = True # If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    'https://dinietts-c33ix.ondigitalocean.app',
] # If this is used, then not need to use `CORS_ALLOW_ALL_ORIGINS = True`
CORS_ALLOWED_ORIGIN_REGEXES = [
    'https://dinietts-c33ix.ondigitalocean.app',
]

