#!/usr/bin/python3
# """ The entry point of the command interpreter""" 

import cmd
 
 
class HBNBCommand(cmd.Cmd):
    """Tha class that Handle the starting 
        and how leave the the program at the end.
    """ 
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    
if __name__ == '__main__':
        HBNBCommand().cmdloop()
