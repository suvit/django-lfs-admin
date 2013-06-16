
from django.conf.urls import patterns, url
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from admin_utils import make_admin_class

from privatesite.admin import CustomAdminSite, CustomModelAdmin

from reviews.models import Review

import lfs.catalog.models  # needed import to remove circular import
from lfs.cart.models import Cart
from lfs.catalog.models import (DeliveryTime, Product, Category,
                                Property, PropertyGroup, StaticBlock, Image)
from lfs.core.models import ActionGroup, Action, Shop
from lfs.customer.models import Customer
from lfs.customer_tax.models import CustomerTax
from lfs.discounts.models import Discount
from lfs.export.models import Export
from lfs.manufacturer.models import Manufacturer
from lfs.marketing.models import FeaturedProduct, Topseller, OrderRatingMail
from lfs.order.models import Order
from lfs.shipping.models import ShippingMethod
from lfs.supplier.models import Supplier
from lfs.payment.models import PaymentMethod
from lfs.page.models import Page
from lfs.tax.models import Tax
from lfs.voucher.models import Voucher


class LFSAdminSite(CustomAdminSite):
    admin_base_template = 'manage/manage_base.html'

    def has_permission(self, request):
        return (request.user.is_active and
                request.user.has_perm('core.manage_shop'))


lfssite = LFSAdminSite(name='manage', app_name='admin')

#http://ionelmc.wordpress.com/2011/06/24/custom-app-names-in-the-django-admin/
class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    def __hash__(self):
        return hash(self.title())

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


# shop
for model in (DeliveryTime, PaymentMethod, Shop, ShippingMethod,
              Tax, CustomerTax, Image, Action, ActionGroup):
    model._meta.app_label = string_with_title(model._meta.app_label,
                                              'Shop')
    lfssite.register(model)

# catalog
for model in Product, Category, Manufacturer, Supplier:
    model._meta.app_label = string_with_title(model._meta.app_label,
                                              'Catalog')
    lfssite.register(model)

# properies
for model in Property, PropertyGroup:
    model._meta.app_label = string_with_title(model._meta.app_label,
                                              'Properties')
    lfssite.register(model)

# content
for model in Page, StaticBlock:
    model._meta.app_label = string_with_title(model._meta.app_label,
                                              'HTML')
    lfssite.register(model)

# clients
for model in Cart, Customer, Order, Review:
    model._meta.app_label = string_with_title(model._meta.app_label,
                                              'Customers')
    lfssite.register(model)

# marketing
for model in FeaturedProduct, Topseller, Discount, Voucher, OrderRatingMail:
    model._meta.app_label = string_with_title(model._meta.app_label,
                                              'Marketing')
    lfssite.register(model)

# utils
for model in Export,:
    model._meta.app_label = string_with_title(model._meta.app_label,
                                              'Utils')
    lfssite.register(model)

make_admin_class('Miscellaneous', patterns("",
    url(r'^$', 'lfs.manage.views.utils.utilities',
        name='utils_miscellaneous_changelist'),
), "utils", site=lfssite)

lfssite.register(User, UserAdmin)
lfssite.register(Group, GroupAdmin)

# help
