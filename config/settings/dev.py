from .base import *  # noqa F403
from .base import BASE_DIR

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATICFILES_DIRS = [
    BASE_DIR / "public",
]

# Configuration of Django-vite
DJANGO_VITE = {
    "default": {"dev_mode": True},
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "{{ secret_key }}"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .local import *
except ImportError:
    pass