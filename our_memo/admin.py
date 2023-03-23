from django.contrib import admin
from .models import Block, Memo
# Register your models here.

#let the admin panel acces and change the instance of Block and Memo
admin.site.register(Block)
admin.site.register(Memo)
