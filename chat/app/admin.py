from django.contrib import admin,sites
from .models import *
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Group)
admin.site.register(GroupMemders)
admin.site.site_header="Chat appliction in django"
admin.site.site_title="Django chat app"

# Register your models here.
