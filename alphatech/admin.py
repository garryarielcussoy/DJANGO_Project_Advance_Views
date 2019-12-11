from django.contrib import admin
from .models import Blog, Mentee, Mentor

# Register your models here.
admin.site.register(Blog)
admin.site.register(Mentee)
admin.site.register(Mentor)