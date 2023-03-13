from django.contrib import admin

from .models import Block, Memo
#makes each block and memo instance manageable from the administration panel
admin.site.register(Block)
admin.site.register(Memo)
