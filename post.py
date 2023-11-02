from dataclasses import dataclass

# class Post:
#     def __init__(self, title, content) -> None:
#         self.title = title
#         self.content = content

#     def to_dict(self):
#         return {
#             'title': self.title,
#             'content': self.content,
#         }


@dataclass
class Post:
    title: str
    content: str

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
        }
