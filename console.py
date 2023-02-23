#!/usr/bin/python3
"""
The entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """ Tha class that Handle the starting
        and how leave the the program at the end.
    """

    list_class = ['BaseModel', 'User', 'State',
                  'City', 'Amenity', 'Place', 'Review']
    list_function = ['create', 'show', 'destroy', 'update', 'all']

    prompt = "(hbnb)"

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """" Do nothing when we have empty line, and/or + space """
        pass

    def do_create(self, line):
        '''Creates a new instance of BaseModel'''

        if len(line) == 0:
            print('** class name missing **')

        elif line not in self.list_class:
            print("** class doesn't exist **")

        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """On va recuper le dictionnaire d'une id d'une class"""
        lines = line.split()

        if not line:
            print("** class name missing **")
            return

        class_name = lines[0]
        if class_name not in self.list_class:
            print("** class doesn't exist **")
            return

        if len(lines) < 2:
            print("** instance id missing **")
            return

        id = lines[1]
        key = "{}.{}".format(class_name, id)
        obj_all = models.storage.all()
        if key not in obj_all:
            print("** no instance found **")
            return
        print(obj_all[key])

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''

        line = line.split()
        obj_dict = storage.all()

        if not line:
            print('** class name missing **')
            return

        if line[0] not in self.list_class:
            print('** class doesn\'t exist **')
            return

        if len(line) < 2:
            print('** instance id missing **')
            return

        k = '{}.{}'.format(line[0], line[1])
        if k in obj_dict:
            del obj_dict[k]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, line):
        '''
        Prints all string representation of all instances based
        or not on the class name.
        '''

        line = line.split()
        obj_dict = storage.all()

        if len(line) == 0:
            print([str(obj) for obj in obj_dict.values()])
        elif line[0] not in self.list_class:
            print('** class doesn\'t exist **')
        else:
            print([str(obj) for obj in obj_dict.values()
                  if type(obj).__name__ == line[0]])

    def do_update(self, line):
        """met à jour une instance en fonction"""

        lines = line.split()
        obj_all = models.storage.all()

        # Vérification de la présence du nom de classe.
        if len(lines) == 0:
            print("** class name missing **")
            return

        class_name = lines[0]
        if class_name not in self.list_class:
            print("** class doesn't exist **")
            return

        # Vérification de la présence de l'id.
        if len(lines) == 1:
            print("** instance id missing **")
            return

        # Vérification de la class
        id = lines[1]
        key = "{}.{}".format(class_name, id)
        if key not in obj_all:
            print("** no instance found **")
            return

        # Vérification de la présence de l'attribut et de sa valeur.
        if len(lines) == 2:
            print("** attribute name missing **")
            return
        if len(lines) == 3:
            print("** value missing **")
            return

        name = lines[2]
        name_value = lines[3]

        setattr(obj_all[key], name, name_value)
        obj_all[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
