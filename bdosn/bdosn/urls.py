
from django.conf.urls import url
from django.contrib import admin

from core.views import sing_up

urlpatterns = [
    url(r'$',sing_up,name='sing_up'),
    url(r'^admin/', admin.site.urls),
]
