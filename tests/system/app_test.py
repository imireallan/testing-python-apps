from unittest import TestCase
from unittest.mock import patch

import app
from blog import Blog

class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mock_input:
            app.menu()
            mock_input.assert_called_with(app.MENU_PROMPT)
    
    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mock_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mock_print_blogs.assert_called_once()

    def test_ask_create_blogs(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ('Test', 'Test user')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))
            
    
    def test_can_print_blogs(self):
        blog = Blog('Blog 1','Allan')
        app.blogs = {'test1': blog}

        with patch('builtins.print') as mock_print:
            app.print_blogs()
            mock_print.assert_called_with(blog.__repr__())