
# Activate pyramid support, in case pyramid is present.
# Silently not do it, if pyramid is not installed.

try:
    import pyramid
    pyramid = pyramid   # shut up pylint
except ImportError:
    pass
else:
    import pyramid_support
    pyramid_support = pyramid_support # shut up pylint

