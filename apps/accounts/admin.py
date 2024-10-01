from django.contrib import admin
from apps.accounts.models import Account
# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')
    

admin.site.register(Account, AccountAdmin)
    