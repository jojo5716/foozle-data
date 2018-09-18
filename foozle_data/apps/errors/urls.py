from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import track_error


urlpatterns = [
    # Template and dynamic views request
    url(r'^capture$', csrf_exempt(track_error), name='foozle_track_error'),
]