import random
from django.http.response import HttpResponse, HttpResponseRedirect
from api.models import Key

__author__ = 'abra'


def _gen_key():
    key = ''
    for i in range(30):
        key += chr(random.randint(0, 25) + ord('A'))
    return key


def register(request):
    while True:
        key = _gen_key()
        if len(Key.objects.filter(key=key)) != 0:
            continue
        obj = Key(key=key)
        obj.save()
        break

    return HttpResponse(key)


def init_chat(request):
    key = 'testotosao'

    return HttpResponseRedirect('/api/chat/' + key)


def chat(request, link):
    # print(link)

    return HttpResponse('chatochat')


def torrent(request):


    return HttpResponse()
