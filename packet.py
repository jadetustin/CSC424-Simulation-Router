from constants import *
from auxiliary import *
from time import time

currentPacketID = STARTING_ID

class Packet:
    
    def __init__(self, randomized_size, randomized_arrival):

        global currentPacketID

        # this constructor assumes that it will receive random vals
        # such will be assured using other calls/wrappers
        self.packetID = currentPacketID
        self.packetSize = randomized_size
        self.arrivalTime = (randomized_arrival / MICROSECONDS_PER_SECOND)
        self.processingTime = (randomized_size / THROUGHPUT)
        self.waitStart = None

        # increment current packetID
        currentPacketID += 1

    def set_waitStart(self):
        
        # called when packet is placed in the PacketQueue
        self.waitStart = time()

    def get_packetID(self):
        return self.packetID

    def get_packetSize(self):
        return self.packetSize

    def get_arrivalTime(self):
        return self.arrivalTime

    def get_processingTime(self):
        return self.processingTime

    def get_waitStart(self):
        return self.waitStart

def create_new_packet(gaussian, exponential):
    
    # calls randomizers to get packet size, arrival time
    # uses the wrappers provided; does not call directly
    size = get_random_packet_size(gaussian)
    arrival = get_random_arrival_time(exponential)

    # call constructor, return the packet to the calling layer
    new_packet = Packet(size, arrival)
    return new_packet

