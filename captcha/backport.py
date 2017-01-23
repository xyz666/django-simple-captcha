from datetime import datetime
from django.conf import settings


try:
    from django.utils.encoding import smart_text
except ImportError:
    from django.utils.encoding import smart_unicode as smart_text


try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url


def get_now():
    try:
        from django.utils import timezone
        return timezone.now()
    except ImportError:
        return datetime.now()
