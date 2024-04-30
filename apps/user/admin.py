from django.contrib import admin
from apps.user.models.user import User
from django.contrib.auth.forms import AdminPasswordChangeForm

class UserAdmin(admin.ModelAdmin):
    change_password_form = AdminPasswordChangeForm

    ordering = ['username']
    list_display = ('username', 'is_superuser')
    search_fields = ('username',)
    list_filter = ('is_superuser',)


admin.site.register(User, UserAdmin)