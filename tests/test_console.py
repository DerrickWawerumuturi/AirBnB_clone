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

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help quit')
            self.assertEqual(f.getvalue().strip(), 'Quit command to exit the program')

    def test_EOF(self):
        """Test EOF command"""
        console_instance = self.create_console_instance()
        self.assertTrue(console_instance.onecmd("EOF"))

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help')
            self.assertIn('EOF', f.getvalue())  # Check if 'EOF' is in the output
            self.assertIn('help', f.getvalue())  # Check if 'help' is in the output
            self.assertIn('quit', f.getvalue()) 

   def test_help_quit(self):
       with patch('sys.stdout', new=StringIO()) as f:
           HBNBCommand().onecmd('help quit')
           self.assertEqual(f.getvalue().strip(), 'Quit command to exit the program')
        
    def test_create_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            output = f.getvalue().strip()
            self.assertIn('User', output) 

    def test_show_user(self):
        """Test show user command"""
        user = User()
        storage.new(user)
        storage.save()
        console_instance = self.create_console_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            console_instance.onecmd(f'show User {user.id}')
            self.assertIn(str(user), f.getvalue())  # Adjust assertion as needed

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
