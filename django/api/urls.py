from django.conf.urls import url, patterns

from api import api


urlpatterns = patterns(
    '',

    url(r'^register/$', api.register),

    url(r'^chat/(?P<addressee>\w*)/recv/$', api.chat_recv),
    url(r'^chat/(?P<addressee>\w*)/send/$', api.chat_send),
    url(r'^chat/(?P<addressee>\w*)/$', api.chat),

    url(r'^notifications/$', api.notifications),
    url(r'^torrent/$', api.torrent),
    url(r'^$', api.main),

)
