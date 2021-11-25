from django.contrib import admin
from .models import Flight, Airport

# Реєструємо ваші моделі.
admin.site.register(Flight)
admin.site.register(Airport)