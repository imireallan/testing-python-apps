from blog import Blog
from post import Post


blogs = dict()
MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post or "q" to quit: '

POST_TEMPLATE = """
---{}---

{}

"""


def menu():
    selection = input(MENU_PROMPT)

    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for blog in blogs.values():
        print(repr(blog))


def ask_create_blog():
    title = input("Enter blog title: ")
    author = input("Enter blog author: ")

    blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input("Enter blog title: ")
    print_posts(blogs[title])


def ask_create_post():
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    blog_title = input("Enter blog title: ")

    post = Post(title, content)
    blog = blogs[blog_title]
    blog.create_post(post)


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


if __name__ == "__main__":
    menu()
