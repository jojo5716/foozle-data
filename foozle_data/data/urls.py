from django.conf.urls import url

from .views import track_data


urlpatterns = [
    # Template and dynamic views request
    url(r'^$', track_data, name='foozle_track_data'),
]