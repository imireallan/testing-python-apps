from dataclasses import dataclass, field
from typing import List
from post import Post

# class Blog:
#     def __init__(self, title, author, posts = None) -> None:
#         self.title = title
#         self.author = author
#         if posts is None:
#             self.posts = []
#         else:
#             self.posts = posts


@dataclass
class Blog:
    title: str
    author: str
    posts: List[Post] = field(default_factory=list)

    def create_post(self, post: Post):
        self.posts.append(post)

    def __str__(self) -> str:
        return f'{self.title} by {self.author} ({len(self.posts)} {"posts" if len(self.posts) == 0 or len(self.posts) > 1 else "post"})'
