from django.contrib import admin

# Register your models here.
from chat.models import user_data,Conversation,Person

admin.site.register(user_data)
admin.site.register(Conversation)
admin.site.register(Person)