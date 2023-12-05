from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import User


UserAdmin.fieldsets[2][1]['fields'] = (
                                    "is_active",
                                    "is_staff",
                                    "is_superuser",
                                    "is_author",
                                    "spetial_user",
                                    "groups",
                                    "user_permissions"
)
UserAdmin.list_display += ("is_author","is_spetial_user")
admin.site.register(User, UserAdmin)
