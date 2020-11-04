from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Group)
admin.site.register(User)
admin.site.register(Item)
admin.site.register(MiningGroupsExperiment)
admin.site.register(Link)
admin.site.register(Transaction)
