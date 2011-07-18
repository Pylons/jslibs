import unittest

class DummyConfig:
    def add_static_view(self, prefix, location):
        self.prefix = prefix
        self.location = location

class TestIncludeJSlibs(unittest.TestCase):
    def _callFUT(self, config, **kwargs):
        from jslibs import include_jslibs
        return include_jslibs(config, **kwargs)

    def test_default_include(self):
        config = DummyConfig()
        self._callFUT(config)
        self.assertEquals(config.prefix, u'jslibs_static')
        self.assertEquals(config.location, u'jslibs:resources/')

    def test_prefixed_include(self):
        config = DummyConfig()
        self._callFUT(config, prefix='aprefix')
        self.assertEquals(config.prefix, u'aprefix')
        self.assertEquals(config.location, u'jslibs:resources/')


class TestMacroDecorator(unittest.TestCase):
    def _makeOne(self):
        class Dummy:
            pass
        from jslibs import jslibsmacros
        cls = Dummy()
        return jslibsmacros(cls)

    def test_reified(self):
        from pyramid.decorator import reify
        decorated = self._makeOne()
        self.assertEquals(type(decorated.jslibs), reify)
        self.assertTrue(hasattr(decorated.jslibs, 'wrapped'))
        self.assertRaises(ValueError, decorated.jslibs.wrapped, decorated)




