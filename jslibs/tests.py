import unittest

from pyramid import testing
from pyramid.url import static_url

class Dummy(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def get(self, value, default):
        return self.__dict__.get(value, default)


class TestMacrosSubscriber(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.begin()

    def tearDown(self):
        self.config.end()

    def test_it(self):
        from jslibs import jslibs_macros_subscriber
        self.config.testing_add_renderer("jslibs:jslibs.pt")
        event = Dummy(request=testing.DummyRequest())
        jslibs_macros_subscriber(event)
        self.assertTrue(hasattr(event.request, 'jslibs'))


class TestIncludeMe(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.begin()

    def tearDown(self):
        self.config.end()

    def test_it_default(self):
        from jslibs import includeme
        request = testing.DummyRequest()
        includeme(self.config)
        url = static_url(u'jslibs:resources/', request)
        self.assertEqual(url, u'http://example.com/jslibs_static/')

    def test_it_with_name(self):
        from jslibs import includeme
        request = testing.DummyRequest()
        self.config.registry.settings['jslibs.static_view_name'] = 'aname'
        includeme(self.config)
        url = static_url(u'jslibs:resources/', request)
        self.assertEqual(url, u'http://example.com/aname/')


