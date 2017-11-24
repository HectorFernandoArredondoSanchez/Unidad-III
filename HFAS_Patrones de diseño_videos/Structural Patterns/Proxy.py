"""Author: Hector Fernando Arredondo Sanchez"""

import time

class Producer:
    """Define the 'resource-intensive' object to instantive!"""

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate as an middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if Producter is available...")

        if self.occupied == 'No':
            #If the producer is available, create a producter object!
            self.producer = Producer()
            time.sleep(2)

            #Make the producer meet te guest!
            self.producer.meet()

        else:
            #Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")

#Instantiate a Proxy
p = Proxy()

#Make the proxy: Artist produce untill producer is available
p.produce()

#Change the state to 'occupied'
p.occupied = 'Yes'


#Make the Producer produce
p.produce()

            
