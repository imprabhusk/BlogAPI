from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(self):
        testuser = User.objects.create(username="testuser", password="abc123")
        testuser.save()

        testpost = Post.objects.create(title="Blog title", body="Body content", author=testuser)
        testpost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        title = f"{post.title}"
        author = f"{post.author}"
        body = f"{post.body}"
        self.assertEqual(title, 'Blog title')
        self.assertEqual(author, 'testuser')
        self.assertEqual(body, "Body content")
