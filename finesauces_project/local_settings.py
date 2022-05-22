"""
This file will contain our sensitive project information like database, email,
and secret payment credentials.
"""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g951h8i@$25)0^q69h9booud&(1o60=2w+1*m4-^&_l&q1uy=h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finesauces',
        'USER': 'finesaucesadmin',
        'PASSWORD': 'hLghG764Hk',
        'HOST': 'localhost',
        'PORT': '5434',
    }
}
