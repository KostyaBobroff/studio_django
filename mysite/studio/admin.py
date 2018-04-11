from django.contrib import admin
from .models import *

admin.site.register([Material, Model, Color, Catalog,Order])