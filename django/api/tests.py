from django.test import TestCase
import requests

_address = 'http://192.168.0.105:8000/'


def _register():
    return requests.get(_address + 'register')


def _notifications(key):
    cookie = {'key': key}
    return requests.get(_address + 'notifications', cookies=cookie)


class TestRegister(TestCase):
    def test(self):
        response = _register()
        self.assertIs(len(response.text), 30)
        self.assertRegex(response.text, '\A[A-Z]{30}\Z')
        pass


class ApiTest(TestCase):
    def setUp(self):
        self.key = _register().text
        pass

    def test_notifications(self):
        response = _notifications(self.key)
        self.assertIs(response.status_code, 200)
        pass





# class RequestTests(TestCase):





class ChatTest(TestCase):
    def register(self):
        # self.key = _register()
        pass


# Create your tests here.
