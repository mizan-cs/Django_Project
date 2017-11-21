
from django.conf.urls import url
from django.contrib import admin
from chat.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login,name='login_views'),
]
