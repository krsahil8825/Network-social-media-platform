from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import ContactMessage


User = get_user_model()


class CoreTests(TestCase):

    def test_index_renders(self):
        resp = self.client.get(reverse("core_index"))
        self.assertEqual(resp.status_code, 200)

    def test_about_renders(self):
        resp = self.client.get(reverse("core_about"))
        self.assertEqual(resp.status_code, 200)

    def test_contact_post_unauthenticated_shows_message(self):
        resp = self.client.post(
            reverse("core_contact"), data={"subject": "Hi", "message": "Hello"}
        )

        # Check the response status code
        self.assertEqual(resp.status_code, 403)

        # Check the context variable directly
        self.assertEqual(
            resp.context["message_unsuccess"],
            "You need to be logged in to send a message.",
        )

    def test_contact_authenticated_creates_message(self):
        u = User.objects.create_user("cuser", "c@example.com", "pw")
        self.client.login(username="cuser", password="pw")
        resp = self.client.post(
            reverse("core_contact"), data={"subject": "Sub", "message": "Body"}
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(ContactMessage.objects.filter(user=u, subject="Sub").exists())

    def test_contact_duplicate_message_shows_already_sent(self):
        u = User.objects.create_user("dup", "d@example.com", "pw")
        ContactMessage.objects.create(user=u, subject="S", message="M")
        self.client.login(username="dup", password="pw")
        resp = self.client.post(
            reverse("core_contact"), data={"subject": "S", "message": "M"}
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "You have already sent this message.")
