from queue import Queue
import random

from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse

from api.models import Pony, Torrent


__author__ = 'abra'

_notification_queues = dict()
_message_queues = dict()


def _gen_key():
    key = ''
    for i in range(30):
        key += chr(random.randint(0, 25) + ord('A'))
    return key


def register(request):
    while True:
        key = _gen_key()
        if len(Pony.objects.filter(key=key)) != 0:
            continue
        else:
            pony = Pony(key=key)
            pony.save()
            return HttpResponse(key)


def chat(request, addressee):
    try:
        key = request.COOKIES['key']
        pony = Pony.get(key=key)

        pony_to = Pony.get(key=addressee)

        print(pony, 'talks to', pony_to)

        if pony not in _notification_queues:
            _notification_queues[pony] = Queue()

        _notification_queues[pony].put({
            'user': pony_to
        })

        return HttpResponse('chatochat')
    except Exception as e:
        print(e)
        return HttpResponseBadRequest('bad')


def chat_recv(request, addressee):
    try:
        key = request.COOKIES['key']
        pony = Pony.get(key=key)

        pony_to = Pony.get(key=addressee)

        if pony not in _message_queues:
            _message_queues[pony] = Queue()

        queue = _message_queues[pony]

        messages = []

        for i in range(3):
            if queue.empty():
                break
            else:
                messages.append(queue.get())

        return JsonResponse({
            'messages': messages
        })
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()


def chat_send(request, addressee):
    try:
        key = request.COOKIES['key']
        pony = Pony.get(key=key)

        pony_to = Pony.get(key=addressee)

        message = request.POST['message']

        if pony_to not in _message_queues:
            _message_queues[pony_to] = Queue()

        _message_queues[pony_to].put(message)

        return HttpResponse('ok')
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()


def torrent(request):
    try:
        key = request.COOKIES['key']
        pony = Pony.objects.get(key=key)

        text = request.POST['text']
        link = request.POST['link']


        torrent = Torrent(pony=pony, text=text, link=link)
        torrent.save()

        return HttpResponse('ok')
    except Exception as e:
        print(e)
        return HttpResponseBadRequest('bad')


def main(request):
    return HttpResponse('main is not here')


def notifications(request):
    try:
        key = request.COOKIES['key']
        pony = Pony.objects.get(key=key)

        if pony not in _notification_queues:
            _notification_queues[pony] = Queue()

        queue = _notification_queues[pony]

        anticipants = []

        for i in range(3):
            if queue.empty():
                break
            else:
                anticipants.append(queue.get())

        return JsonResponse({
            'notifications': anticipants
        })
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()
