
def include_jslibs(config, prefix=u'jslibs_static'):
    """
    A hook for inclusion in a Pyramid app.

    config
        An instance of ``pyramid.config.Configurator`` from the calling app.
    prefix
        A string to use in the url.

        Default: ``u"jslibs_static"``


    Example:

    .. code-block:: python


        from jslibs import include_jslibs

        ...

        def main(global_config, **settings):
            ...
            config = Configurator(...)
            config.scan('myapp')
            include_jslibs(config, prefix='aprefix')
            ...

    """
    config.add_static_view(prefix, u'jslibs:resources/')


def jslibsmacros(cls):
    """
    a decorator for use with the TemplateAPI pattern. Use it to
    decorate the TemplateAPI class to add jslibs to your TemplateAPI

    ..code-block:: python

        @jslibsmacros
        class TemplateAPI(API):
            @reify
            def main(self):
                r = get_renderer('myapp.views:templates/main.pt')
                return r.implementation()

            @reify
            def macros(self):
                r = get_renderer('myapp.views:templates/macros.pt')
                return r.implementation().macros

    You can then call it in a template like so

    ..code-block:: xml

          <metal:resources metal:use-macro="tmpl.jslibs['google-cdn']" />
    """
    from pyramid.renderers import get_renderer
    from pyramid.decorator import reify
    @reify
    def jslibs(self):
        r = get_renderer('jslibs:jslibs.pt')
        return r.implementation().macros
    cls.jslibs = jslibs
    return cls

