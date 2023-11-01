from unittest import TestCase
from post import Post

class PostTest(TestCase):

    def setUp(self):
        self.title = 'Test'
        self.content = 'Test Content'
        self.post = Post(self.title, self.content)

    def test_initializes_post(self):
        self.assertEqual(self.title, self.post.title)
        self.assertEqual(self.content, self.post.content)

    def test_to_dict(self):
        expected_dict = {'title': self.title, 'content': self.content}

        self.assertDictEqual(expected_dict, self.post.to_dict())


