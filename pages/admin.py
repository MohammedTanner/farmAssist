from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TankReading)
admin.site.register(Meetup)
admin.site.register(MeetupComment)
admin.site.register(AuthUser)