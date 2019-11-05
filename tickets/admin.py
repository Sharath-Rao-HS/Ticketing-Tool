from django.contrib import admin
from tickets.models import project,Employee,ticketHeader,ticketlog

admin.site.register(project)
admin.site.register(Employee)
admin.site.register(ticketHeader)
admin.site.register(ticketlog)