from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^muse/', include('muse.urls')),
    url(r'^admin/', admin.site.urls),
]
