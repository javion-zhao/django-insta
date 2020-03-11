from django.contrib import admin

# Register your models here.
from Insta.models import  Post,InstaUser,Like,Comment


admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(InstaUser)