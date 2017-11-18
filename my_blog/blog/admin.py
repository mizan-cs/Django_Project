from django.contrib import admin

from blog.models import Post_DB,Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category']


admin.site.register(Post_DB,BlogAdmin)
admin.site.register(Category)


