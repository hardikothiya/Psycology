from django.contrib import admin
from app_demo.models import User, UserTemp, ContactUs, Mood

admin.site.register(User)
admin.site.register(UserTemp)
admin.site.register(Mood)
admin.site.register(ContactUs)
