"""
Django settings for proyecto_catedra project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
from django.urls import reverse_lazy
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k(m#+e2p=40ezs%y99+-)&+(41o!2iz#x+wys^lljca^q=c*h#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.5']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'gestioninstitucion',
    'gestionresponsableinstitucional',
    'gestionautor',
    'gestiontutor',
    'gestiontipoproyecto',
    'gestionareaconocimiento',
    'gestioncarrera',
    'gestionproyecto',
    'gestionimagnes',
    'gestionactas',
    'gestionarchivos',
    'gestionayuda',
    'gestionayuda1',
    'gestionayuda2',
    'gestionayuda3',
    'gestionayuda4',
    'gestionayuda5',
    'gestionayuda6',
    'gestionayuda7',
    'gestionayuda8',
    'gestionayuda9',
    'gestionayuda10',
    'social_django',
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'proyecto_catedra.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [r'C:/Users/villa/Downloads/proyecto_catedra/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto_catedra.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Seguimiento_Proyectos',
        'USER': 'Seguimiento_Proyectos',
        'PASSWORD': 'Seguimiento_Proyecto2019',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

LOGIN_URL= reverse_lazy('login')


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-sp'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = 'C:/Users/villa/Downloads/proyecto_catedra/media'
MEDIA_URL = "/media/"

EMAIL_USE_TLS = True
EMAIL_HOST =  'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'seguimientoproyectos2019@gmail.com'
EMAIL_HOST_PASSWORD= 'Seguimiento_Proyectos2019'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'homepage'
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '122507428928-c7c9smcs7k8vajssrkna1sob8o2566j4.apps.googleusercontent.com'
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'dj6dyDeZkSGzFfAtNYMrcvqH'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '604096279264-9vveool58nvipkh9vq59f3t8nr849fim.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'k6IHijbWBU-DwyXApEuSfYsq'

#SOCIAL_AUTH_GITHUB_KEY ='35364a1e1d7a3533dba3'
#SOCIAL_AUTH_GITHUB_SECRET = 'f18efbaa6daf80c7e08e72b1c721e304874ec95e'
SOCIAL_AUTH_GITHUB_KEY ='ee0d76d261070bcb8e10'
SOCIAL_AUTH_GITHUB_SECRET = '0f52ff30a45ce825af28bdb8200d3e5b6066c822'