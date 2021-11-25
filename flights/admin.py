from django.contrib import admin
from .models import Flight, Airport, Passenger

# Реєструємо ваші моделі.
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger)