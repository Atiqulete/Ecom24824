from django.contrib import admin
from .models import RegisterForm
from user_app.models import profile

# Register your models here.

admin.site.register(RegisterForm)
admin.site.register(profile)
