SECRET_KEY = "django-insecure-jv!jxo%un3wse2^#s2_e$awvo1-cpb1z-)f7o14nry-9se7=ui"

INSTALLED_APPS = [
    "django_dynamodb_cache",
]

CACHES = {
    "default": {"BACKEND": "django_dynamodb_cache.backend.DjangoCacheBackend"},
    "replica": {"BACKEND": "django_dynamodb_cache.backend.DjangoCacheBackend"},
}
USE_TZ = False
