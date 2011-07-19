jslibs
==========

Summary
-------

``jslibs`` is a small package with few dependencies, aimed at providing
a high quality, curated set of Javascript packages for Pyramid
projects. In essence, a group of people have taken the work they are
already doing, then pushing it out to share with others. This work
includes use of `Juicer <https://github.com/cjohansen/juicer>`_ to
increase responsiveness of apps.

Installation
------------

Install using setuptools, e.g. (within a virtualenv)::

  $ easy_install jslibs

Setup
-----

Once ``jslibs`` is installed, you only need include it:

.. code-block:: python

    ...

    def main(global_config, **settings):
        ...
        config = Configurator(...)
        config.scan('myapp')
        config.include('jslibs')
        ...

The macros will be available in templates like so:

.. code-block:: xml

    <metal:resources metal:use-macro="request.jslibs['google-cdn']" />


More Information
----------------

.. toctree::
   :maxdepth: 1

   api.rst
   glossary.rst
   overview.rst

Reporting Bugs / Development Versions
-------------------------------------

Visit http://github.com/Pylons/jslibs to download development or
tagged versions.

Visit http://github.com/Pylons/jslibs/issues to report bugs.

Indices and tables
------------------

* :ref:`glossary`
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
