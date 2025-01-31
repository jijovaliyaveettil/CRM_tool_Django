from django.contrib import admin
from .models import Lead, Agent, User

admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(User)

# Register your models here.
