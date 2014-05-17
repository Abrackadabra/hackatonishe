from queue import Queue
import random

from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_POST, require_GET

from api.models import Pony, Torrent


__author__ = 'abra'

_notification_queues = dict()
_message_queues = dict()


def _gen_key():
    key = ''
    for i in range(30):
        key += chr(random.randint(0, 25) + ord('A'))
    return key


@require_GET
def register(request):
    while True:
        key = _gen_key()
        if len(Pony.objects.filter(key=key)) != 0:
            continue
        else:
            pony = Pony(key=key)
            pony.save()
            return HttpResponse(key)


@require_GET
def chat(request, addressee):
    try:
        key = request.COOKIES['key']
        pony = Pony.objects.get(key=key)

        pony_to = Pony.objects.get(key=addressee)

        print(pony, 'talks to', pony_to)

        if 'no_notification' not in request.GET:
            if pony not in _notification_queues:
                _notification_queues[pony] = Queue()

            queue = _notification_queues[pony]

            queue.put({
                'user': pony_to
            })

        return HttpResponse('chatochat')
    except Exception as e:
        print(e)
        return HttpResponseBadRequest('bad')


@require_POST
def chat_send(request, addressee):
    try:
        key = request.COOKIES['key']
        print('key', key)

        pony = Pony.objects.get(key=key)
        print('pony', pony)

        pony_to = Pony.objects.get(key=addressee)
        print('pony_to', pony_to)

        message = request.POST['message']
        print('message', message)

        queue_id = (pony, pony_to)

        print('queue_id', queue_id)

        if queue_id not in _message_queues:
            _message_queues[queue_id] = Queue()

        _message_queues[queue_id].put(message)

        return HttpResponse('ok')
    except Exception as e:
        print(e)
        return HttpResponseBadRequest('bad')


@require_GET
def chat_recv(request, addressee):
    try:
        key = request.COOKIES['key']
        pony = Pony.objects.get(key=key)

        pony_from = Pony.objects.get(key=addressee)

        queue_id = (pony_from, pony)

        print('queue_id', queue_id)

        if queue_id not in _message_queues:
            _message_queues[queue_id] = Queue()

        queue = _message_queues[queue_id]

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


@require_POST
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


@require_GET
def main(request):
    return HttpResponse('main is not here')


@require_GET
def notifications(request):
    try:
        key = request.COOKIES['key']
        pony = Pony.objects.get(key=key)

        if pony not in _notification_queues:
            _notification_queues[pony] = Queue()

        queue = _notification_queues[pony]

        notifications = []

        for i in range(3):
            if queue.empty():
                break
            else:
                notifications.append(queue.get())

        return JsonResponse({
            'notifications': notifications
        })
    except Exception as e:
        print(e)
        return HttpResponseBadRequest('bad')
