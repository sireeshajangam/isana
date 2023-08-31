from django.contrib import admin

# Register your models here.

from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
# from import_export.admin import ImportExportModelAdmin
from django import forms


app_models = apps.get_app_config('adminapp').get_models()
for model in app_models:
	try:
	    admin.site.register(model)
	except AlreadyRegistered:
	    pass