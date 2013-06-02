from django.conf.urls import patterns, include, url
from django.conf import settings

from lfs_admin.admin import lfssite

urlpatterns = patterns('',
    url(r'^manage/admin/', include(lfssite.urls)),
    url(r'^manage/', include('lfs.manage.urls')),
    url(r'^', include('lfs.core.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns("",
    (r'^assets/(?P<path>.*)$', 'django.views.static.serve',
     { 'document_root': settings.MEDIA_ROOT }),
)
