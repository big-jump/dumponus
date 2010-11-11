from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'upload.views.upload', name="upload"),
    url(r'^u/$', 'upload.views.upload_list', name="upload-list"),
    url(r'^(?P<id>\d+)/$', 'upload.views.upload_detail', name="upload-detail"),
	url(r'^admin/', include(admin.site.urls), name="admin"),
)
