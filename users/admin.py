from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    change = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'age']

admin.site.register(CustomUser, CustomUserAdmin)