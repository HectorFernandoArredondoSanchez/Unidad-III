"""Author: Hector Fernando Arredondo Sanchez"""
"""it is a software design pattern that defines a dependency
of type one to many between objects, so that when one of the objects
changes its state, it notifies this change to all the dependents."""

class Subject(object): #Respresentes what is being 'observed'

    def __init__(self):
        self._observers = [] #This where references to all the observers are being kept
                             #Note that this is a one-to-many relationship: there will be one subject to be observed by multiple_observers

    def attach(self, observer):
        if observer not in self._observers: #If the observer is not already in the obsevers list
            self._observers.append(observer)#Append the observer to the list

    def detach(self, observer): #Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:#For all the observers in the list
            if modifier != observer:#Don't notify the observer who is actually updating the temperature
                observer.update(self)#Alert the observers!


class Core(Subject): #Inherits from the @Subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name #Set the name of the core
        self._temp = 0 #Initialize the temperature of the core

    @property #Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter #Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        #Notify the observers whenever somebody changes the core temperature


class TempViewer:
    def update(self, subject): #Allert method that is invoked when notify() method in a concrete subject is invoked
        print("Temperature Viewer: {} has temperature {}".format(subject._name, subject,_temp))


#Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

#Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

#Let's create our observers to the first core
c1.attach(v1)
c1.attach(v2)

#Let's create the temperature to the first core
c1.temp = 80
c1.temp = 90
