django-lfs-admin
================

Integration between django-lfs and django.contrib.admin

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/suvit/django-lfs-admin/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

INSTALLATION
------------

Install from pypi, with pip::

    pip install django-lfs-admin

Add ``lfs_admin`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = ("lfs_admin", ) + ('lfs', ...)
    
Please note, that ``lfs_admin`` app must be upper
then ``lfs`` in ``INSTALLED_APPS`` list
to overload ``manage/manage_base.html`` template

Add ``apptemplates.Loader`` to TEMPLATE_LOADER setting.
this is needed to overload templates


USAGE
-----

    from lfs_admin.admin import lfssite
    from myapp.models import MyModel

    lfssite.register(MyModel)


TODO
----

* write model admin for shop (fieldsets, portlets)
* write model admin for shipping method (criterions, prices)
* write model admin for payment method (criterions, prices)
* write model admin for category (tree view)
* write model admin for product (tabs, different subtype, ...)
* write model admin for root and other pages (portlets)
* write docs
* write tests
* add travis

USEFULL LINKS
---------------

[CHANGES](CHANGELOG.rst)
