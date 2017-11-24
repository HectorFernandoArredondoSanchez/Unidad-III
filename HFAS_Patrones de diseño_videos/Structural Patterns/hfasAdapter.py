

class Korean:
    """Korean speaker"""

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class British:
    """English speaker"""
    def __init__(self):
        self.name = "British"

    #Note the different method name here!
    def speak_english(self):
        return "Hello!"

class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of method"""
        self._object = object

        #Add a new dictionary item taht establishes the papping betwen the generic method name: speaak() and the concrete method
        #For example, speak() will be translated to sepeak_korean()if the mapping say so
        self.__dict__.update(adapted_method)
    def __getattr__(self, attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)

#List to store speaker objects
objects = []

#Create a korean object
korean = Korean()

#Create a British object
british = British()

#append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))



