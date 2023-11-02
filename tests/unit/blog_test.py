from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    def setUp(self) -> None:
        self.title = "Django"
        self.author = "Allan"
        self.posts = [{"title": "Django signals", "content": "They are awesome"}]

    def test_initialize_blog_with_empty_posts(self):
        blog = Blog(self.title, self.author)

        self.assertEqual(self.author, blog.author)
        self.assertListEqual([], blog.posts)

    def test_initialize_blog_with_posts(self):
        blog = Blog(self.title, self.author, self.posts)

        self.assertEqual(self.author, blog.author)
        self.assertListEqual(self.posts, blog.posts)

    def test_create_posts(self):
        blog = Blog(self.title, self.author)
        post = Post("New post", "New content")

        blog.create_post(post)

        self.assertEqual(1, len(blog.posts))

    def test_str_method(self):
        blog = Blog(self.title, self.author, self.posts)
        blog2 = Blog("New title", "Maggy", [self.posts, self.posts])

        self.assertEqual("Django by Allan (1 post)", blog.__str__())
        self.assertEqual("New title by Maggy (2 posts)", blog2.__str__())
