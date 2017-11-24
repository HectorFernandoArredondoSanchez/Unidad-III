"""Author: Hector Fernando Arredondo Sanchez"""

class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"

class PetStore:
    """PetStore hoses our Abstract Facototy"""

    def __init__(self, pet_factory=None):
        """pet_factory ins Abstrac factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Unity method to display the details of the objects returned by the DogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))


#Create to concrete factory
factory = DogFactory() 

#Create a petStore housing our Abstract Factory
shop = PetStore(factory)

#Invoke the utility method to show the datails of our pet
shop.show_pet()
        
