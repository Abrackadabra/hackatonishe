from django.conf.urls import url, patterns

from api import api


urlpatterns = patterns(
    '',

    url(r'^register/', api.register),
    url(r'^chat/(?P<addressee>.*)/', api.chat),
    url(r'^chat/(?P<addressee>.*)/recv/', api.chat_recv),
    url(r'^chat/(?P<addressee>.*)/send/', api.chat_send),
    url(r'^notifications/', api.notifications),
    url(r'^torrent/', api.torrent),
    url(r'^/', api.main),

)
