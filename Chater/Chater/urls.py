from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout
from chat.views import login_view, registration_view, home_view

urlpatterns = [
    url ( r'^admin/', admin.site.urls ),
    url ( r'^$', home_view, name='HomePage' ),
    url ( r'^login/$', login_view, name='login_views' ),
    url ( r'^sing-up/$', registration_view, name='registration_view' ),
    url ( r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout' )
]
