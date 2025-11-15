from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import ContactMessage


User = get_user_model()


class CoreTests(TestCase):

    def test_index_renders(self):
        # index page should load
        resp = self.client.get(reverse("core_index"))
        self.assertEqual(resp.status_code, 200)

    def test_about_renders(self):
        # about page should load
        resp = self.client.get(reverse("core_about"))
        self.assertEqual(resp.status_code, 200)

    def test_contact_post_unauthenticated_shows_message(self):
        # posting without login should fail
        resp = self.client.post(
            reverse("core_contact"), data={"subject": "Hi", "message": "Hello"}
        )

        # expect forbidden
        self.assertEqual(resp.status_code, 403)

        # check error message in context
        self.assertEqual(
            resp.context["message_unsuccess"],
            "You need to be logged in to send a message.",
        )

    def test_contact_authenticated_creates_message(self):
        # authenticated user can send a message
        u = User.objects.create_user("cuser", "c@example.com", "pw")
        self.client.login(username="cuser", password="pw")
        resp = self.client.post(
            reverse("core_contact"), data={"subject": "Sub", "message": "Body"}
        )
        self.assertEqual(resp.status_code, 200)

        # message should be stored in DB
        self.assertTrue(ContactMessage.objects.filter(user=u, subject="Sub").exists())

    def test_contact_duplicate_message_shows_already_sent(self):
        # user already has same message in DB
        u = User.objects.create_user("dup", "d@example.com", "pw")
        ContactMessage.objects.create(user=u, subject="S", message="M")
        self.client.login(username="dup", password="pw")

        # posting duplicate message
        resp = self.client.post(
            reverse("core_contact"), data={"subject": "S", "message": "M"}
        )

        self.assertEqual(resp.status_code, 200)

        # should show duplicate warning
        self.assertContains(resp, "You have already sent this message.")
