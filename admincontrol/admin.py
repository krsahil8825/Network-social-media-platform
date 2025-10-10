from django.contrib import admin
from core.models import ContactMessage
from users.models import User


# This will modify the admin interface
admin.site.site_header = "Network Admin Control"
admin.site.index_title = "Admin Panel"
admin.site.site_title = "Network Admin"


# users app models
admin.site.register(User)

# core app models
admin.site.register(ContactMessage)
