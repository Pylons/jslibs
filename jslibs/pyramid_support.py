from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.renderers import get_renderer

def includeme(config):
    """
    A hook for inclusion in a Pyramid app. You can set a
    static_view_name by assigning a value to
    ``jslibs.static_view_name`` in settings Defaults to:
    ``u"jslibs_static"``

    config
        An instance of ``pyramid.config.Configurator`` from the calling app.


    Example:

    .. code-block:: python

        ...

        def main(global_config, **settings):
            ...
            config = Configurator(...)
            config.scan('myapp')
            config.include('jslibs')
            ...
    """
    view_name = config.registry.settings.get(u'jslibs.static_view_name',
                                             u'jslibs_static')
    config.add_static_view(view_name, u'jslibs:resources/')
    config.scan('jslibs')

@subscriber(NewRequest)
def jslibs_macros_subscriber(event):
    """
    Adds the macros to the request object so it can then be called in
    a template like so:

    .. code-block:: xml

          <metal:resources metal:use-macro="request.jslibs['google-cdn']" />
    """
    r = get_renderer('jslibs:jslibs.pt')
    event.request.jslibs = r.implementation().macros
