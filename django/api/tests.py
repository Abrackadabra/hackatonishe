from django.test import TestCase
import requests

_address = 'http://192.168.0.105:8000/'


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
    params = {'message': message}
    return requests.post(_address + 'chat/' + your_key + '/send', cookies=cookies, params=params)


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
        self.assertIs(response.status_code, 200)
        pass

# Create your tests here.
