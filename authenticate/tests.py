from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticateTests(TestCase):

    # Registration
    def test_register_creates_user(self):
        resp = self.client.post(
            reverse("register"),
            data={
                "username": "tester",
                "email": "t@example.com",
                "password": "pass1234",
                "confirmation": "pass1234",
            },
        )
        # should redirect on success
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(User.objects.filter(username="tester").exists())

    def test_register_missing_username_shows_error(self):
        resp = self.client.post(
            reverse("register"),
            data={
                "username": "",
                "email": "t@example.com",
                "password": "pass1234",
                "confirmation": "pass1234",
            },
        )
        # stays on page with error
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Username is required.")

    # Login
    def test_login_success(self):
        User.objects.create_user("loginuser", "l@example.com", "pw")
        resp = self.client.post(
            reverse("login"), {"username": "loginuser", "password": "pw"}
        )
        # valid login → redirect
        self.assertEqual(resp.status_code, 302)

    def test_login_missing_password_shows_error(self):
        resp = self.client.post(reverse("login"), {"username": "no_pw", "password": ""})
        # missing password → show error
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Password is required.")

    # Logout
    def test_logout_redirects(self):
        User.objects.create_user("out", "o@example.com", "pw")
        self.client.login(username="out", password="pw")
        resp = self.client.get(reverse("logout"))
        # logout should redirect
        self.assertEqual(resp.status_code, 302)
