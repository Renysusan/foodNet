from django.contrib import admin

from . import models

'''
PRADEEP: TODO
'''
class CuisineMemberInline(admin.TabularInline):
    model = models.CuisineMember



admin.site.register(models.Cuisine)
