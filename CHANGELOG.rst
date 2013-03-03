Changelog
=========

Current
-------

- nothing yet


0.3 (2013-03-03)
----------------

- Check if django.contrib.sites is enabled (thanks to Rodrigo Primo)
- Django 1.5 compatibility (Documentation and tests)
- Added ``absolute_future`` template tag library
  (match ``{% load url from future %}`` syntax).
- drop support for Python 2.6 (test only)


0.2.2 (2012-11-18)
------------------

- Handle template tag `as` syntax


0.2.1 (2012-11-10)
------------------

- Fix packaging


0.2 (2012-11-10)
----------------

- ``{% site %}`` fallback on http protocol if ``request`` is missing.


0.1 (2012-06-10)
----------------

- Initial release
