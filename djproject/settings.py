"""Django settings for djproject project.Generated by 'django-admin startproject' using Django 1.11.16.For more information on this file, seehttps://docs.djangoproject.com/en/1.11/topics/settings/For the full list of settings and their values, seehttps://docs.djangoproject.com/en/1.11/ref/settings/"""import osimport django_herokuimport dj_database_url# Build paths inside the project like this: os.path.join(BASE_DIR, ...)BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# Quick-start development settings - unsuitable for production# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/# SECURITY WARNING: keep the secret key used in production secret!SECRET_KEY = '=d0ej@w6p@qxe6&3az9b*%bds9_z9%z=&8)ndw89l#1)q@iy5g'# SECURITY WARNING: don't run with debug turned on in production!DEBUG = TrueALLOWED_HOSTS = ['*']STATIC_URL = '/static/'STATIC_ROOT = os.path.join(BASE_DIR, 'static')STATICFILES_DIRS = []db_from_env = dj_database_url.config()DATABASES = { 'default': dj_database_url.config() }#Application definitionSTATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'INSTALLED_APPS = [    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',    'rest_framework',    'rest_framework.authtoken',    'corsheaders',    'farmer',    'employee',    'livestock',    'vaccination']MIDDLEWARE = [    'django.middleware.security.SecurityMiddleware',    'django.contrib.sessions.middleware.SessionMiddleware',    'django.middleware.common.CommonMiddleware',    'django.middleware.csrf.CsrfViewMiddleware',    'django.contrib.auth.middleware.AuthenticationMiddleware',    'django.contrib.messages.middleware.MessageMiddleware',    'django.middleware.clickjacking.XFrameOptionsMiddleware',    'corsheaders.middleware.CorsMiddleware',    'django.middleware.common.CommonMiddleware',]ROOT_URLCONF = 'djproject.urls'TEMPLATES = [    {        'BACKEND': 'django.template.backends.django.DjangoTemplates',        'DIRS': [os.path.join(BASE_DIR,'templates')],        'APP_DIRS': True,        'OPTIONS': {            'context_processors': [                'django.template.context_processors.debug',                'django.template.context_processors.request',                'django.contrib.auth.context_processors.auth',                'django.contrib.messages.context_processors.messages',            ],        },    },]WSGI_APPLICATION = 'djproject.wsgi.application'# Database# https://docs.djangoproject.com/en/1.11/ref/settings/#databasesDATABASES = {    'default': {        'ENGINE': 'django.db.backends.sqlite3',        'NAME': os.path.join(BASE_DIR, 'vaccindb'),    }}# Password validation# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validatorsAUTH_PASSWORD_VALIDATORS = [    {        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',    },]CORS_ORIGIN_ALLOW_ALL = TrueAUTHENTICATION_BACKENDS = (    ('django.contrib.auth.backends.ModelBackend'),)# Internationalization# https://docs.djangoproject.com/en/1.11/topics/i18n/LANGUAGE_CODE = 'ru'TIME_ZONE = 'Asia/Almaty'USE_I18N = TrueUSE_L10N = TrueUSE_TZ = True# Static files (CSS, JavaScript, Images)# https://docs.djangoproject.com/en/1.11/howto/static-files/STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'REST_FRAMEWORK = {    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',    'PAGE_SIZE': 100,    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),    #'DEFAULT_AUTHENTICATION_CLASSES': (     #   'rest_framework.authentication.TokenAuthentication',    #),    #'DEFAULT_PERMISSION_CLASSES': (    #    'rest_framework.permissions.IsAuthenticated',    #),}django_heroku.settings(locals())