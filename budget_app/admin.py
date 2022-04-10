from django.contrib import admin
from budget_app.models import Income, Expense

# Register your models here.
admin.site.register(Income)
admin.site.register(Expense)