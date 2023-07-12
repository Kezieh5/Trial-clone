#!/usr/bin/python3
import cmd

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

"""Console for
management of
hbnb data
"""


class HBNBCommand(cmd.Cmd):
    """Type class HBNB CLI"""
    prompt = '(hbnb) '
    __classes = {
        'BaseModel',
        'Amenity',
        'City',
        'State',
        'User',
        'Review',
        'Place'
    }

    def emptyline(self):
        """ empty line"""
        pass

    def do_quit(self, line):
        """Exit shell"""
        return True

    def do_EOF(self, line):
        """Exit shell"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
