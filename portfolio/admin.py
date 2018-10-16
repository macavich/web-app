from django.contrib import admin

from .models import Manager, Instrument, Question, Portfolio, Position, Price

admin.site.register(Manager)
admin.site.register(Instrument)
admin.site.register(Portfolio)
admin.site.register(Position)
admin.site.register(Price)

admin.site.register(Question)
