from data_collection import *
import queue

class PacketQueue:

    def __init__(self, size):

        # we will not reinvent the wheel; using the library Queue class
        # here, None (and thus a no-args constructor) means an infinite queue
        if size is None: 
            self.internalQueue = queue.Queue()
        else:
            self.internalQueue = queue.Queue(size)

    def enqueue(self, packet, data_module):

        # places a packet in the queue
        # other functions are responsible for not calling this if full
        self.internalQueue.put(packet)
        packet.set_waitStart()

        # send the size to the data collection module for validation
        # we only do this here since maxQueueSize should not be bigger on dequeue
        current_size = self.get_size()
        data_module.validate_max_queue(current_size)

    def dequeue(self):

        # remove the next packet from the queue and return
        # other functions are responsible for not calling this if empty
        next_packet = self.internalQueue.get()
        return next_packet

    def is_empty(self):
        status = self.internalQueue.empty()
        return status

    def is_not_empty(self):
        status = self.internalQueue.empty()
        if status == True:
            return False
        return True

    def is_full(self):
        status = self.internalQueue.full()
        return status

    def get_size(self):
        size = self.internalQueue.qsize()
        return size

def create_new_packet_queue(size = None):
    new_packet_queue = PacketQueue(size)
    return new_packet_queue
