from django.contrib import admin
from .models import CustomUser, Store, Like, Favourite, Comment


admin.site.register(CustomUser)
admin.site.register(Store)
admin.site.register(Like)
admin.site.register(Favourite)
admin.site.register(Comment)