"""Author: Hector Fernando Arredondo Sanchez"""
"""it is a pattern of behavior that avoids coupling the sender of a request to its
receiver giving more than one object the possibility of responding to a request."""

class Handler: #Abstract handler
    """Abstract handler"""
    def __init__(self, successor):
        self._successor = successor #Define who is the next handler
    
    def handle(self, request):
        handled = self._handle(request)#If handled, stop here

        #Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Most provide implementation in subclass!")


class ConcreteHandler1(Handler): #Inherits from the abstract handler
    """Concrete handler 1"""
    def _handle(self, request):
        if 0 < request <= 10: #Provide a condition for handling
            print("Request {} handled in handler 1".format(request))
            return True #Indicates that the request has been handled

class DefaultHandler(Handler): #inherits from the abstract handler
    """Default handler"""

    def _handle(self, request):
        """If there is no handler available"""
        #No condition checking since this is a handler
        print("End of chai, no handler for {}".format(request))
        return True #Indicates that the request has been handled

class Client: #Using handlers
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))#Create handlers and use them in a squence you want
        # Note that the default hadler has no successor

    def delegate(self, requests): #Send your request one at time for handlers to handle
        for request in requests:
            self.handler.handle(request)

#Create a client
c = Client()

#Create requests
requests = [2, 5, 30]

#Send requests
c.delegate(requests)
