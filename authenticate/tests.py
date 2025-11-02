from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class AuthenticateTests(TestCase):
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
        # registration redirects to core_index
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
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Username is required.")

    def test_login_success(self):
        u = User.objects.create_user("loginuser", "l@example.com", "pw")
        resp = self.client.post(
            reverse("login"), data={"username": "loginuser", "password": "pw"}
        )
        # login redirects to core_index
        self.assertEqual(resp.status_code, 302)

    def test_login_missing_password_shows_error(self):
        resp = self.client.post(
            reverse("login"), data={"username": "no_pw", "password": ""}
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Password is required.")

    def test_logout_redirects(self):
        u = User.objects.create_user("out", "o@example.com", "pw")
        self.client.login(username="out", password="pw")
        resp = self.client.get(reverse("logout"))
        self.assertEqual(resp.status_code, 302)
