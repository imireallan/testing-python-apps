from unittest import TestCase
from unittest.mock import patch

import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch("builtins.input", return_value="q") as mock_input:
            app.menu()
            mock_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_ask_create_blog(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ("c", "Test title", "Test Author", "q")
            app.menu()
            self.assertIsNotNone(app.blogs["Test title"])

    def test_menu_calls_print_blogs(self):
        with patch("builtins.input") as mock_input:
            with patch("app.print_blogs") as mock_print_blogs:
                mock_input.side_effect = ("l", "q")
                app.menu()
                mock_print_blogs.assert_called_once()

    def test_menu_calls_ask_read_blog(self):
        with patch("builtins.input") as mock_input:
            with patch("app.ask_read_blog") as mock_ask_read_blog:
                mock_input.side_effect = ("r", "q")
                app.menu()
                mock_ask_read_blog.assert_called_once()

    def test_menu_calls_ask_create_post(self):
        with patch("builtins.input") as mock_input:
            with patch("app.ask_create_post") as mock_ask_create_post:
                mock_input.side_effect = ("p", "q")
                app.menu()
                mock_ask_create_post.assert_called_once()

    def test_ask_create_blogs(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ("Test", "Test user")
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get("Test"))

    def test_can_print_blogs(self):
        blog = Blog("Blog 1", "Allan")
        app.blogs = {"test1": blog}

        with patch("builtins.print") as mock_print:
            app.print_blogs()
            mock_print.assert_called_with(blog.__repr__())

    def test_can_ask_read_blog(self):
        blog = Blog("Blog 1", "Allan")
        app.blogs = {"Blog 1": blog}
        with patch("builtins.input", return_value="Blog 1"):
            with patch("app.print_posts") as mock_print_posts:
                app.ask_read_blog()
                mock_print_posts.assert_called_once_with(blog)

    def test_print_posts(self):
        blog = Blog("Blog 1", "Allan")
        post = Post("Test", "testing")
        blog.create_post(post)

        with patch("app.print_post") as mock_print_post:
            app.print_posts(blog)
            mock_print_post.assert_called_once_with(blog.posts[0])

    def test_print_post(self):
        post = Post("Test", "testing")
        expected_print = """
---Test---

testing

"""
        with patch("builtins.print") as mock_print:
            app.print_post(post)
            mock_print.assert_called_once_with(expected_print)

    def test_ask_create_post(self):
        blog = Blog("Blog 1", "Allan")
        app.blogs = {"Blog 1": blog}

        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ("Test Post", "Test Content", "Blog 1")

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, "Test Post")
