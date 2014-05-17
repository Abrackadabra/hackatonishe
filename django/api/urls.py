from django.conf.urls import url, patterns

from api import api


urlpatterns = patterns(
    '',

    url(r'^register/', api.register),
    url(r'^chat/(?P<link>.*)', api.chat),
    url(r'^init_chat/', api.init_chat),

)
