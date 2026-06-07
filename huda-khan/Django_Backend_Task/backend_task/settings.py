from pathlib import Path
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-(o8sl(wtg%u&pg&0@7h=d70afkmf0-tmkn2@bt7q)49g#dbtc8'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users',
    'ai.apps.AiConfig',
    'payments',

    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_task.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend_task.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

cloudinary.config(
    cloud_name='dihmc17lx',
    api_key='586511789288376',
    api_secret='wAfdROREKB7QkmeY9GkqLz4mdi4'
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dihmc17lx',
    'API_KEY': '586511789288376',
    'API_SECRET': 'wAfdROREKB7QkmeY9GkqLz4mdi4',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hudaakhter09@gmail.com'
EMAIL_HOST_PASSWORD = 'PUT_YOUR_NEW_APP_PASSWORD_HERE'
EMAIL_USE_TLS = True

GEMINI_API_KEY = 'AQ.Ab8RN6KKNK5st-hydVzU3NQxXu7et_3FOHE7PNbf1i6cfc31Bw'

STRIPE_SECRET_KEY = 'sk_test_51TfeUdJLbB54AX11SEV4kZW2Oz5TMerrYF7uBwySbVW3kQkm1OtCS76TL8fne0GGpRuA5h7l6gDe8VaVr5SHlzn800SrV8F448'

OPENROUTER_API_KEY = "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"