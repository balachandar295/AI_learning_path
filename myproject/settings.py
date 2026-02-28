from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%yd-i3#a-ywff0@u31n+n72a-q*@qo%+4(a$us#t0v(8tujfc-'

DEBUG = True

ALLOWED_HOSTS = ['*']

# 1. Register Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # Marakama idhai podunga
    'core',         # Unga app name
]

# 2. Add CORS Middleware (Top-la irukanum)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # <-- Idhu kandippa irukanum
    'django.contrib.messages.middleware.MessageMiddleware',      # <-- Idhuvum kandippa irukanum
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Inga dhaan namba path sollanum
        'DIRS': [BASE_DIR / 'core' / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 4. Frontend-ku permission tharudhu
CORS_ALLOW_ALL_ORIGINS = True 

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'core' / 'static']
CSRF_TRUSTED_ORIGINS = ['https://dreamy-correctly-jewell.ngrok-free.dev']

import os
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ALLOWED_HOSTS = ['ai-learning-path-6.onrender.com', 'localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['https://ai-learning-path-6.onrender.com']