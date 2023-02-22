#!/usr/bin/python3
"""
The entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Tha class that Handle the starting
        and how leave the the program at the end.
    """

    list_class = ['BaseModel']
    list_function = ['create']

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

        elif line not in HBNBCommand.list_class:
            print("** class doesn't exist **")

        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        '''
        Prints the string representation of an instance based on
        the class name and id
        '''

        line = line.split()
        obj_dict = storage.all()

        if len(line) == 0:
            print('** class name missing **')

        elif line[0] not in HBNBCommand.list_class:
            print('** class doesn\'t exist **')

        elif len(line) < 2:
            print('** instance id missing **')

        else:
            k = '{}.{}'.format(line[0], line[1])
            if k in obj_dict:
                print(obj_dict[k])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''

        line = line.split()
        obj_dict = storage.all()

        if len(line) == 0:
            print('** class name missing **')

        elif line[0] not in HBNBCommand.list_class:
            print('** class doesn\'t exist **')

        elif len(line) < 2:
            print('** instance id missing **')

        else:
            k = '{}.{}'.format(line[0], line[1])
            if k in obj_dict:
                del obj_dict[k]
                storage.save()
            else:
                print('** no instance found **')

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True

    def do_all(self, line):
        """  """
        lines = line.split()
        obj_dict = storage.all()
        if len(lines) == 0:
            print([str(obj) for obj in obj_dict.values()])
        elif lines[0] not in self.class_name:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in obj_dict.values()
                   if type(obj).__name__== lines[0]])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
