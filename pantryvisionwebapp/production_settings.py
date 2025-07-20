import os
from .settings import *

# Override settings for production
DEBUG = False

# Add Vercel domain to allowed hosts
ALLOWED_HOSTS = ['.vercel.app', '.now.sh', 'localhost', '127.0.0.1']

# Override middleware to include WhiteNoise for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configure static files for production
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Only include STATICFILES_DIRS if the directory exists
static_dir = os.path.join(BASE_DIR, 'static')
if os.path.exists(static_dir):
    STATICFILES_DIRS = [static_dir]
else:
    STATICFILES_DIRS = []

# Media files configuration for production
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Database configuration for production
# Note: Vercel doesn't support persistent storage, consider using a cloud database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Use in-memory database for serverless
    }
}

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Environment variables for API keys
LOGMEAL_API_TOKEN = os.environ.get('LOG_MEAL_TOKEN', 'your-default-token')
PALM_API_KEY = os.environ.get('PALM_API_KEY', 'your-default-key') 