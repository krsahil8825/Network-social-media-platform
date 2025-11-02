from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import admin
from users.models import User, Profile, Follow
from feed_and_posts.models import Post, Comment
from core.models import ContactMessage


class AdmincontrolTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_admin_site_metadata(self):
        self.assertIn("Network Admin", admin.site.site_title)

    def test_user_model_registered_in_admin(self):
        self.assertIn(User, admin.site._registry)

    def test_profile_model_registered_in_admin(self):
        self.assertIn(Profile, admin.site._registry)

    def test_post_model_registered_in_admin(self):
        self.assertIn(Post, admin.site._registry)

    def test_contactmessage_model_registered_in_admin(self):
        self.assertIn(ContactMessage, admin.site._registry)
