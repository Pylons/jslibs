===============
jslibs Overview
===============

Web projects frequently use external Javascript libraries such as
jQuery.  Getting these libraries into your project and publishing
them as static resources isn't terribly hard.  But doing a quality
job is a fair amout of work.

jslibs is a small package with few dependencies, aimed at providing a
high quality, curated set of Javascript packages for Pyramid projects.
In essence, a group of people have taken the work they are already
doing, then pushing it out to share with others.  This work includes
use of Juicer to increase responsiveness of apps.

Is
==

- Curated, maintained, documented, tested

- Multiple versions of the external libraries "we" use

- Friendly to far-future expires strategies via version numbers in
  files

- Easy to use for Pyramid projects

- Various combinations of combined/minified using Juicer

Is Not
======

- The one, official way to do things.  If you don't like it, ignore
  it or do your own, it's not that big of a deal.

- Every single Javascript package, only the ones "we" use

- Framework-y and complicated

Might Be
========

- Framework-y, if we want to cover Deform's need for a resource
  registry

How It Works
============

The jslibs team maintain a project in the Pylons GitHub with the
documentation and machinery to spew out packaged-up distributions of
stuff.  The package, when checked out by us, will pull in various
Javascript projects as "externals".  Thus, we won't have jQuery checked
in directly into Pylons/jslibs.

We'll then run some scripts which use Juicer to produce different
flavors of stuff: teeny tiny, normal, and jumbo.  After that, we'll
push an egg to PyPI, and people can then make the egg a dependency of
their project. The egg will likely contain all versions of
previously-packaged stuff.

More info available in :doc:`usage`.
