# django imports
from django import template
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext as _

from lfs_admin.admin import lfssite

register = template.Library()


@register.inclusion_tag('manage/main_menu.html', takes_context=True)
def main_menu(context):
    app_list = lfssite.index(context['request']).context_data['app_list']

    new_app_list = SortedDict()
    for app in app_list:
        if app['name'] in new_app_list:
            new_app_list[app['name']]['models'].extend(app['models'])
        else:
            new_app_list[app['name']] = app
    context['new_app_list'] = new_app_list.values()
    if context['title'] == _('Site administration'):
        context['app_list'] = context['new_app_list']
    return context
