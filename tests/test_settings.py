from django.conf import settings

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":tests:"}}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

SECRET_KEY = "fake_secret_key"

INSTALLED_APPS = ("npi_field", "tests",)
