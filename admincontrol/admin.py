from django.contrib import admin
from users.models import User


# This will modify the admin interface
admin.site.site_header = "Network Admin Control"
admin.site.index_title = "Admin Panel"
admin.site.site_title = "Network Admin"

# Register your models here.
admin.site.register(User)
