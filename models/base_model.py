#!/usr/bin/python3
"""Le but de ce code est de créer une classe BaseModel qui servira de modèle pour les autres
classes de notre projet. La classe BaseModel contient des attributs tels que l'id, la date de 
création et de mise à jour, ainsi que des méthodes pour convertir ses attributs en 
dictionnaire et pour créer une nouvelle instance à partir d'un dictionnaire."""


"""
Dans le projet AirBnB, la classe BaseModel sert de modèle de base pour toutes les autres classes 
de l'application. Toutes les classes de l'application héritent des attributs et des méthodes 
définis dans la classe BaseModel, ce qui permet de standardiser le comportement et la structure 
de toutes les classes.

Grâce à cela, toutes les classes héritent d'attributs communs tels que l'identifiant unique, 
la date de création et de mise à jour, ainsi que des méthodes comme la conversion en dictionnaire
et la sauvegarde dans un fichier JSON. Cela permet de faciliter la gestion et la manipulation 
des données de l'application.
"""

"""
Sans kwargs :

instance = BaseModel()
print(instance.id) # imprime un uuid unique
print(instance.created_at) # imprime la date de création de l'instance
print(instance.updated_at) # imprime la date de modification de l'instance (identique à la date de création car l'instance vient d'être créée)

"""

"""
Avec kwargs :
kwargs = {
  "id": "00000000-0000-0000-0000-000000000001",
  "created_at": "2022-02-22T22:22:22.222222",
  "updated_at": "2022-02-22T22:22:22.222222",
  "custom_attribute": "custom_value"
}

instance = BaseModel(**kwargs)
print(instance.id) # imprime 00000000-0000-0000-0000-000000000001 (l'id a été assigné dans le dictionnaire)
print(instance.created_at) # imprime l'objet datetime correspondant à "2022-02-22T22:22:22.222222" (converti depuis la chaîne de caractères dans le dictionnaire)
print(instance.updated_at) # imprime l'objet datetime correspondant à "2022-02-22T22:22:22.222222" (converti depuis la chaîne de caractères dans le dictionnaire)
print(instance.custom_attribute) # imprime "custom_value" (l'attribut n'est pas assigné par défaut, mais est présent dans le dictionnaire et est ajouté à l'instance BaseModel)
"""

import uuid
from datetime import datetime
import models

class BaseModel:

    """On va etuliser args et kwargs pour
        la création d'une base d'un model"""
    def __init__(self, *args, **kwargs):
            """Dans la méthode __init__(), on vérifie si l'argument kwargs est présent, ce qui
              indique que l'objet doit être créé à partir d'un dictionnaire. Si kwargs n'est pas vide, 
              on parcour chaque paire clé-valeur dans le dictionnaire. Si la clé est created_at 
              ou updated_at, on converti la valeur de la chaîne de caractères en objet datetime. 
              Ensuite, vous utilisez la méthode setattr() pour définir l'attribut de l'objet correspondant 
              à la clé avec la valeur."""
            if kwargs:
                 for key, value in kwargs.items():
                      if key == 'created_at' or key == 'updated_at':
                           """convertie l'objet en datatime"""
                           value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                      if key != '__class__':
                           setattr(self, key, value)
            if not kwargs:
                """id permettra d'avoir un identifiant unique transformer en str a chaque
                instancation de class BaseModel"""
                self.id = str(uuid.uuid4())

                """attribuer la date et l'heure a la création de instance class BaseModel"""
                self.created_at = datetime.now()

                """Permet d'attribut la date et l'heure quand une instance et mofifier"""
                self.updated_at = self.created_at

                """ajoute metode self(new) sur storage"""
                models.storage.new(self)

    def __str__(self):
        """Methode special qui return la chaine suivante"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):

        """A chaque fois qu'il y aura une modification, l'attribut sera mise à jour"""
        self.updated_at = datetime.now()

        """appel metode pour storage dans le fichier file_storage.PY
        pour transformer les valeur en dictionner et les enregistrer dans 
        un fichier jsopn comme ca on tous les instance de la class"""
        models.storage.save()

    def to_dict(self):
        """On va return un dictionner avec les noms (clées) et les valeur des attributs
        pour que sa soit plus lisible avant de l'enregistrer dans notre fichier json"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
