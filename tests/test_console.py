import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand  # Assuming HBNBCommand is defined in console module
from models.user import User     # Assuming User is imported from models.user module
from models import storage       # Assuming storage is imported from models module

class TestConsole(unittest.TestCase):
    """Test cases for the console module"""

    def setUp(self):
        """Set up method to reload storage before each test"""
        storage.reload()

    def create_console_instance(self):
        """Helper method to create a console instance"""
        return HBNBCommand()

    def test_quit(self):
        """Test quit command"""
        console_instance = self.create_console_instance()
        self.assertTrue(console_instance.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        console_instance = self.create_console_instance()
        self.assertTrue(console_instance.onecmd("EOF"))

    def test_help(self):
        """Test help command"""
        console_instance = self.create_console_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            console_instance.onecmd('help')
            self.assertEqual(f.getvalue(), 'Documented commands (type help <topic>):\n\nEOF  help  quit\n')

    def test_help_quit(self):
        """Test help quit command"""
        console_instance = self.create_console_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            console_instance.onecmd('help quit')
            self.assertEqual(f.getvalue(), 'Quit command to exit the program\n')

    def test_create_user(self):
        """Test create user command"""
        console_instance = self.create_console_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            console_instance.onecmd('create User')
            self.assertIn('User', f.getvalue())  # Adjust assertion as needed

    def test_destroy_user(self):
        """Test destroy user command"""
        user = User()
        storage.new(user)
        storage.save()
        console_instance = self.create_console_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            console_instance.onecmd(f'destroy User {user.id}')
            self.assertEqual('', f.getvalue())

    def test_all_users(self):
        """Test all users command"""
        user1 = User()
        user2 = User()
        storage.new(user1)
        storage.new(user2)
        storage.save()
        console_instance = self.create_console_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            console_instance.onecmd('all User')
            self.assertIn(str(user1), f.getvalue())
            self.assertIn(str(user2), f.getvalue())

