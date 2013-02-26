Django Absolute
===============

.. image:: https://secure.travis-ci.org/noirbizarre/django-absolute.png
   :target: http://travis-ci.org/noirbizarre/django-absolute

Django Absolute provides context processors and template tags to use full absolute URLs in templates.

Installation
------------

You can install Django Absolute with pip:

.. code-block:: bash

    pip install django-absolute

or with easy_install:

.. code-block:: bash

    easy_install django-absolute


Add ``absolute`` to your ``settings.INSTALLED_APPS``.


Context processor
-----------------

Add ``absolute.context_processors.absolute`` to your ``settings.TEMPLATE_CONTEXT_PROCESSORS``.
Django Absolute context processor depends on request context processor:

.. code-block:: python

    from django.conf import global_settings

    TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'absolute.context_processors.absolute',
    )

Then you can access the following variables in your templates:

* ``ABSOLUTE_ROOT``: full absolute root URL (without trailing slash) based on incoming request
* ``ABSOLUTE_ROOT_URL``: full absolute root URL (with trailing slash) based on incoming request
* ``SITE_ROOT``: full absolute root URL (without trailing slash) based on current Django Site
* ``SITE_ROOT_URL``: full absolute root URL (with trailing slash) based on current Django site


Template tags
-------------

Django absolute provide 2 template tags:

* ``absolute``: acts like ``url`` but provide a full URL based on incoming request.
* ``site``: acts like ``url`` but provide a full URL based on current Django Site.

To use theses template tags, you need to load the ``absolute`` template tag library.

.. code-block:: html+django

    {% load absolute %}

    {% url index %}
    {% absolute index %}
    {% site index %}

These template tags have exactly the same syntax as ``url``, including the "`as`" syntax:

.. code-block:: html+django

    {% absolute index as the_url %}
    {{ the_url }}


If you use Django 1.5, you need to use the "new-style" url syntax (quoted parameters):

.. code-block:: html+django

    {% load absolute %}

    {% url "index" %}
    {% absolute "index" %}
    {% site "index" %}

    {% absolute "index" as the_url %}
    {{ the_url }}


If you want to match the "new-style" syntax in Django < 1.5 you need to load ``absolute_future`` instead (same behavior as ``{% load url from future %}``).

.. code-block:: html+django

    {% load url from future %}
    {% url "index" %}

    {% load absolute_future %}

    {% absolute "index" %}
    {% site "index" %}

    {% absolute "index" as the_url %}
    {{ the_url }}

For more informations, see the `Django 1.5 release notes <https://docs.djangoproject.com/en/dev/releases/1.5/>`_.
