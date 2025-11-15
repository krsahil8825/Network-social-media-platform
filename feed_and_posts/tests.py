from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from feed_and_posts.models import Post, Comment


User = get_user_model()


class FeedAndPostsTests(TestCase):

    def test_post_str(self):
        # model __str__ should include expected text
        u = User.objects.create_user("puser", "p@example.com", "pw")
        p = Post.objects.create(user=u, title="T", content="C")
        self.assertIn("Post Title", str(p))

    def test_create_post_view_creates(self):
        # logged-in user can create a post
        u = User.objects.create_user("creator", "cr@example.com", "pw")
        self.client.login(username="creator", password="pw")
        resp = self.client.post(
            reverse("create_post"), data={"title": "Hello", "content": "Body"}
        )
        # should redirect after creation
        self.assertEqual(resp.status_code, 302)
        # post saved in DB
        self.assertTrue(Post.objects.filter(user=u, title="Hello").exists())

    def test_like_post_toggle(self):
        # like action should toggle and return JSON
        u = User.objects.create_user("liker", "l@example.com", "pw")
        p = Post.objects.create(user=u, title="T2", content="C2")
        self.client.login(username="liker", password="pw")
        resp = self.client.post(reverse("like_post", kwargs={"request_slug": p.slug}))
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        # should indicate successful like
        self.assertTrue(data.get("liked"))
        self.assertEqual(data.get("total_likes"), 1)

    def test_comment_on_post_creates_comment(self):
        # submitting a comment should create DB entry
        u = User.objects.create_user("comm", "co@example.com", "pw")
        p = Post.objects.create(user=u, title="T3", content="C3")
        self.client.login(username="comm", password="pw")
        resp = self.client.post(
            reverse("comment_on_post", kwargs={"request_slug": p.slug}),
            data={"content": "Nice"},
        )
        self.assertEqual(resp.status_code, 302)
        # comment saved
        self.assertTrue(Comment.objects.filter(post=p, content="Nice").exists())

    def test_delete_post_not_owner_redirects_404(self):
        # non-owner trying to delete should redirect
        owner = User.objects.create_user("owner", "o@example.com", "pw")
        other = User.objects.create_user("other", "r@example.com", "pw")
        p = Post.objects.create(user=owner, title="Del", content="X")
        self.client.login(username="other", password="pw")
        resp = self.client.get(reverse("delete_post", kwargs={"request_slug": p.slug}))
        # expected redirect to 404 handler
        self.assertEqual(resp.status_code, 302)
