
def include_jslibs(config, prefix='jslibs_static'):
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
    config.add_static_view(prefix, 'jslibs:resources/')

