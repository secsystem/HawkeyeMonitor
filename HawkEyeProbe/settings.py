"""
Django settings for HawkEyeProbe project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n248!m-$1+xdgin0^926ispy(_$a@4*w^%p_c0@(&6t8_b7=j*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
REGEX_URL = r'^{url}$'  # url作严格匹配
# 白名单
SAFE_URL =[
    r'/welcome/',
    '/user/',
    '/admin/',
]
# 设置网站根地址
WEB_URL = 'http://localhost:8000'

# 设置登录初始路径
LOGIN_URL = '/welcome/'

# 设置登录session有效时间
SESSION_COOKIE_AGE = 60*360
# 设置session关闭浏览器失效
SESSION_EXPIRE_AT_BROWSER_CLOSE  = True


# 定义session 键：
# 保存用户权限url列表
# 保存 权限菜单 和所有 菜单
SESSION_PERMISSION_URL_KEY = 'spuk'
SESSION_MENU_KEY = 'smk'
ALL_MENU_KEY = 'amk'
PERMISSION_MENU_KEY = 'pmk'


#设置邮箱
EMAIL_HOST = 'smtp.163.com'          #SMTP地址
EMAIL_PORT = 25                 #SMTP端口
EMAIL_HOST_USER = 'wangshuchn@163.com'    #我自己的邮箱
EMAIL_HOST_PASSWORD = 'wshu!@#456'         #我的邮箱密码
EMAIL_SUBJECT_PREFIX = u'[HawkEye]'      #为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True               #与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
#管理员站点
SERVER_EMAIL = 'xxxxx'
DEFAULT_FROM_EMAIL = '鹰眼监控平台<wangshuchn@163.com>'

#设置队列存储
BROKER_URL = 'amqp://user:psd@xx.xx.xx.xx/vhost'    #设置与rabbitmq一致
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'RBAC',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'RBAC.middleware.rbac.RbacMiddleware',
]

ROOT_URLCONF = 'HawkEyeProbe.urls'

#配置静态文件路径
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'HawkEyeProbe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'HawkEye',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB',
            'charset': 'utf8',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
STATICFILES_DIRS=(
                   os.path.join(BASE_DIR, "static"),
                   )