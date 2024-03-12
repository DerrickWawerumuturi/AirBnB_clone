#!/usr/bin/python3
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage

class TestConsole(unittest.TestCase):

    def setup(self):
        storage. Reload()

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help')
            self.assertEqual(f.getvalue(), 'Documented commands (type help <topic>):\n\nEOF  help  quit\n')

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('help quit')
            self.assertEqual(f.getvalue(), 'Quit command to exit the program\n')

    def test_create_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            self.assertEqual(f.getvalue(), '** id ** 1\n')

    def test_show_user(self):
        user = User(id=1, email='test@test.com', password='test')
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User 1')
            self.assertEqual(f.getvalue(), str(user))

    def test_destroy_user(self):
        user = User(id=1, email='test@test.com', password='test')
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User 1')
            self.assertEqual(f.getvalue(), '')

    def test_all_users(self):
        user1 = User(id=1, email='test1@test.com', password='test1')
        user2 = User(id=2, email='test2@test.com', password='test2')
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all User')
            self.assertEqual(f.getvalue(), str(user1) + '\n' + str(user2))

if __name__ == '__main__':
    unittest.main()
