"""Author: Hector Fernando Arredondo Sanchez"""

class Borg:
    """Borg class marking class attributes global"""
    _shared_state = {} #Atribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state #Make it an attribute dictionary


class Singleton(Borg): #Inherits from Borg class
    """This class now shares all its attributes among its vaious instances"""
    #This essentially makes the singleton objects an objects-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        #Update the atribute dictionary by iserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        #Returns the attribute dictionary for printing
        return str(self._shared_state)


#Let´s create a singleton object and add our first acronym
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
#Print the object
print(x)
#Let´s create singleton object and if it refers to the same attribute dictionary by adding acronym
y = Singleton(SNMP = "Simple Network Managment Protocol")
#Print the object
print(y)
