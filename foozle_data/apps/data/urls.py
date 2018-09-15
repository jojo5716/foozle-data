from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import track_data, track_action


urlpatterns = [
    # Template and dynamic views request
    url(r'^track$', csrf_exempt(track_data), name='foozle_track_data'),
    url(r'^actions$', csrf_exempt(track_action), name='foozle_track_action'),
]