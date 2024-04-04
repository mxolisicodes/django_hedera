
from core.project.settings import ENV,DEBUG
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV.config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = ENV.config('DEBUG', cast=bool)
DEBUG = DEBUG

ALLOWED_HOSTS = ENV.config('ALLOWED_HOSTS', cast=ENV.Csv())