from django.contrib import admin
from core.models import ContactMessage
from feed_and_posts.models import Post, Comment
from users.models import User, Follow, Profile


# This will modify the admin interface
admin.site.site_header = "Network Admin Control"
admin.site.index_title = "Admin Panel"
admin.site.site_title = "Network Admin"


# users app models
class UserView(admin.ModelAdmin):
    list_display = ("username", "email", "is_active", "is_staff", "date_joined")
    search_fields = ("username", "email")
    list_filter = ("is_active", "is_staff", "date_joined")


admin.site.register(User, UserView)


class ProfileView(admin.ModelAdmin):
    list_display = ("user", "bio", "avatar_link")
    search_fields = ("user__username", "bio")
    list_filter = ("user__is_active",)


admin.site.register(Profile, ProfileView)


class FollowView(admin.ModelAdmin):
    list_display = ("follower", "following")
    search_fields = ("follower__username", "following__username")
    list_filter = ("follower__is_active", "following__is_active")


admin.site.register(Follow, FollowView)


# core app models
class ContactMessageView(admin.ModelAdmin):
    list_display = ("__str__", "user__username", "user__email", "created_at")
    search_fields = ("user__username", "subject", "message")
    list_filter = ("created_at", "user__is_active")


admin.site.register(ContactMessage, ContactMessageView)


# feed_and_posts app models
class PostView(admin.ModelAdmin):
    list_display = ("__str__", "user", "created_at")
    search_fields = ("user__username", "title", "content")
    list_filter = ("created_at",)
    filter_horizontal = ("likes",)


admin.site.register(Post, PostView)


class CommentView(admin.ModelAdmin):
    list_display = ("__str__", "user", "post", "created_at")
    search_fields = ("user__username", "post__title", "content")
    list_filter = ("created_at",)


admin.site.register(Comment, CommentView)
