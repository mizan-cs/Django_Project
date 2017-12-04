
from django.conf.urls import url
from django.contrib import admin

from blog.views import blog_home,blog_post

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',blog_home,name='Blog_Home_Page'),
    url(r'^post/(?P<pk>[0-9]+)/$',blog_post,name='Blog_Post_Page'),

]
