from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import Profile, Follow

User = get_user_model()


class UsersTests(TestCase):

    def test_profile_str(self):
        # Ensure __str__ returns expected text
        u = User.objects.create_user("upro", "u@example.com", "pw")
        p = Profile.objects.create(user=u, bio="hello")
        self.assertIn("Profile of", str(p))

    def test_follow_toggle_creates_and_deletes(self):
        # Check follow toggle adds/removes follow relation
        a = User.objects.create_user("a", "a@example.com", "pw")
        b = User.objects.create_user("b", "b@example.com", "pw")
        self.client.login(username="a", password="pw")

        # First toggle -> follow
        resp = self.client.post(reverse("follow_toggle", kwargs={"username": "b"}))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Follow.objects.filter(follower=a, following=b).exists())

        # Second toggle -> unfollow
        resp = self.client.post(reverse("follow_toggle", kwargs={"username": "b"}))
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Follow.objects.filter(follower=a, following=b).exists())

    def test_edit_profile_updates_bio(self):
        # Verify bio update works
        u = User.objects.create_user("edit", "e@example.com", "pw")
        self.client.login(username="edit", password="pw")

        resp = self.client.post(
            reverse("edit_profile", kwargs={"username": "edit"}),
            data={"title": "", "content": "New bio"},
        )

        # Should redirect on success
        self.assertEqual(resp.status_code, 302)

        p = Profile.objects.get(user=u)
        self.assertEqual(p.bio, "New bio")

    def test_profile_view_returns_context(self):
        # Ensure profile view returns expected context
        u = User.objects.create_user("view", "v@example.com", "pw")
        other = User.objects.create_user("other", "o@example.com", "pw")
        self.client.login(username="other", password="pw")

        resp = self.client.get(reverse("user_profile", kwargs={"username": "view"}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn("this_user", resp.context)

    def test_follow_toggle_cannot_follow_self(self):
        # Prevent self-following
        u = User.objects.create_user("selfu", "s@example.com", "pw")
        self.client.login(username="selfu", password="pw")

        resp = self.client.post(reverse("follow_toggle", kwargs={"username": "selfu"}))
        self.assertEqual(resp.status_code, 400)
