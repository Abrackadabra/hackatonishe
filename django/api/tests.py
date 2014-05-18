from django.test import TestCase
import requests
import json

_address = 'http://abra0.com:8000/'


def _register():
    return requests.get(_address + 'register')


def _notifications(my_key):
    cookies = {'key': my_key}
    return requests.get(_address + 'notifications', cookies=cookies)


def _recv(my_key, your_key):
    cookies = {'key': my_key}
    return requests.get(_address + 'chat/' + your_key + '/recv', cookies=cookies)


def _send(my_key, your_key, message):
    cookies = {'key': my_key}
    data = {'message': message}
    return requests.post(_address + 'chat/' + your_key + '/send', cookies=cookies, data=data)


def _torrent(my_key, text, link):
    cookies = {'key': my_key}
    data = {'text': text, 'link': link}
    return requests.post(_address + 'torrent', cookies=cookies, data=data)


def _chat(my_key, your_key, no_notifications):
    cookies = {'key': my_key}
    params = {}
    if no_notifications:
        params['no_notifications'] = ""

    return requests.get(_address + 'chat/' + your_key, cookies=cookies, params=params)


class TestRegister(TestCase):
    def test(self):
        response = _register()
        self.assertIs(len(response.text), 30)
        self.assertRegex(response.text, '\A[A-Z]{30}\Z')
        pass


class ApiTest(TestCase):
    def setUp(self):
        self.my_key = _register().text
        self.your_key = _register().text
        pass

    def test_notifications(self):
        response = _notifications(self.my_key)
        self.assertIs(response.status_code, 200)
        pass

    def test_recv(self):
        response = _recv(self.my_key, self.your_key)
        self.assertIs(response.status_code, 200)
        pass

    def test_send(self):
        response = _send(self.my_key, self.your_key, 'kakoi-to_pidor')
        print(response.text)
        self.assertIs(response.status_code, 200)
        pass

    def test_send_recv(self):
        message = 'kakoi-to_pidor'
        _send(self.my_key, self.your_key, message)
        response = _recv(self.your_key, self.my_key)
        self.assertEqual(json.loads(response.text)['messages'][0], message)

    def test_torrent(self):
        response = _torrent(self.my_key, "MyLittlePony.REPACK.720pp.S03E99.ZVERRELIZ.mkv", "thepiratebay.huehue/...")
        self.assertIs(response.status_code, 200)
        pass

    def test_chat(self):
        response = _chat(self.my_key, self.your_key, True)
        self.assertIs(response.status_code, 200)
        response = _chat(self.my_key, self.your_key, False)
        self.assertIs(response.status_code, 200)
        pass

# Create your tests here.
