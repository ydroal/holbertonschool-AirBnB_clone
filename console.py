import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys
import models


"""File file_storage.PY"""


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand qui herite cmd.Cmd"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    tab = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_create(self, arg):
        """Crée une nouvelle instance de BaseModel
           et l'enregistre dans le fichier JSON"""

        # Récupère la liste des mots dans la commande de création
        args = arg.split()

        if not args:
            # Si la commande est vide, affiche un message d'erreur
            print("** class name missing **")

        elif args[0] not in self.tab:
            # Si la classe n'existe pas, affiche un message d'erreur
            print("** class doesn't exist **")

        else:
            newInstance = eval(arg)()
            newInstance.save()
            print(newInstance.id)

    def do_show(self, arg):
        """On va recuper le dictionnaire d'une id d'une class"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.tab:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]
        key = "{}.{}".format(class_name, id)
        obj_all = models.storage.all()
        if key not in obj_all:
            print("** no instance found **")
            return
        print(obj_all[key])

    def do_destroy(self, arg):
        """On va suprimer les instance d'une class
           et enregister dans le fichier json"""

        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.tab:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]
        key = "{}.{}".format(class_name, id)
        obj_all = models.storage.all()
        if key not in obj_all:
            print("** no instance found **")
            return

        del obj_all[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""

        args = arg.split()
        obj_all = models.storage.all()

        # Si aucun argument n'est fourni, on affiche toutes les instances.
        if not len(args):
            print([str(obj_all[key]) for key in obj_all])

        # Si un nom de classe est fourni, on affiche toutes les instances.
        elif args[0] in self.tab:
            print([str(obj_all[key])
                   for key in obj_all if key.startswith(args[0] + ".")])

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """met à jour une instance en fonction"""

        args = arg.split()
        obj_all = models.storage.all()

        # Vérification de la présence du nom de classe.
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.tab:
            print("** class doesn't exist **")
            return

        # Vérification de la présence de l'id.
        if len(args) == 1:
            print("** instance id missing **")
            return

        # Vérification de la class
        id = args[1]
        key = "{}.{}".format(class_name, id)
        if key not in obj_all:
            print("** no instance found **")
            return

        # Vérification de la présence de l'attribut et de sa valeur.
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        name = args[2]
        name_value = args[3]

        setattr(obj_all[key], name, name_value)
        obj_all[key].save()
