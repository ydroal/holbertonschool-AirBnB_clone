#!/usr/bin/python3
"""
The entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Tha class that Handle the starting
        and how leave the the program at the end.
    """

    list_class = ['BaseModel', 'User']
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

        elif line not in self.list_class:
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

        elif line[0] not in self.list_class:
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

        elif line[0] not in self.list_class:
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
        line = line.split()
        obj_dict = storage.all()
        k = '{}.{}'.format(line[0], line[1])

        if len(line) == 0:
            print('** class name missing **')

        elif line[0] not in self.list_class:
            print('** class doesn\'t exist **')

        elif len(line) < 1:
            print('** instance id missing **')

        elif k not in obj_dict:
            print('** no instance found **')

        elif len(line) < 2:
            print('** attribute name missing **')

        elif len(line) == 3:
            print('** value missing **')

        else:
            update_attr = line[2]
            update_value = line[3]
            setattr(obj_dict[k], update_attr, update_value)
            obj_dict[k].save()

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
