from django.contrib import admin
from first_app.models import AccessRecord,Topic,WebPage,Users,Register
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)
admin.site.register(Users)
admin.site.register(Register)
