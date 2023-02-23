#!/usr/bin/python3
"""model de storage"""


from models.base_model import BaseModel
import json
import os
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """class pour file storage"""

    """__file_path est un chemin vers un fichier JSON dans lequel nous enregistrerons 
    les objets. Lorsque nous créons une instance de la classe FileStorage"""

    __file_path = 'file.json'

    """__objects est un dictionnaire qui stocke les objets créés par l'application 
    en utilisant leur nom de classe et leur identifiant unique.
    BaseModel.1234 
    En utilisant ces deux variables, la classe FileStorage est capable de stocker 
    et de récupérer les objets créés par l'application."""

    __objects = {}

    """La méthode all() de la classe FileStorage retourne le dictionnaire 
    des objets stockés dans __objects."""

    def all(self):
        """return dictionary of __objects"""
        return FileStorage.__objects


    """La méthode new(self, obj) de la classe FileStorage est une méthode qui permet d'ajouter 
    un objet au dictionnaire __objects de la classe FileStorage
    "BaseModel.123456": {"id": "123456", "name": "example", "created_at": "2022-02-22T12:00:00", "updated_at": "2022-02-22T12:00:00"}"""

    """Cette methode est appeler a la acreation de l'object dans la methode BaseMethode"""
    def new(self, obj):
        """set in __objects with key"""
        if obj:
            """BaseModel.123456": {"id": "123456", "name": "example", "created_at": "2022-02-22T12:00:00", "updated_at": "2022-02-22T12:00:00"}"""
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj


    """La méthode save() de la classe FileStorage a pour objectif de sérialiser 
    (convertir en format JSON) le dictionnaire __objects de la classe FileStorage 
    et d'écrire le résultat de cette sérialisation dans un fichier."""

    """Cette methode est appeler par BaseModel qui elle est appeler par 
    La console lors de la creation du modele avec la commande Create BaseModel"""
    def save(self):
        """serializes __objects to the JSON"""
        jdict = {}
        for keys, values in FileStorage.__objects.items():
            jdict[keys] = values.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(jdict, file)

    """Cette méthode permet de désérialiser le fichier JSON en objets Python 
    et de les stocker dans le dictionnaire __objects."""

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as file:
                new_object_dict = json.load(file)
            for keys, val in new_object_dict.items():
                obj = eval(val['__class__'])(**val)
                FileStorage.__objects[keys] = obj
