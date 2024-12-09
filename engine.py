from event import *
from constants import *
from time import time

class Engine:

    def __init__(self):
        self.packet = None
        self.busy = False
        self.busyStart = None

    def set_packet(self, packet):
        self.packet = packet
        self.busy = True
        self.busyStart = time()

    def clear_busy(self, data_module):        
        self.busy = False
        data_module.validate_engine_usage(self.busyStart)

    def is_not_busy(self):
        status = self.busy
        if status == True:
            return False
        return True

    def service_next_packet(self, packet_queue, event_queue):

        # checking if busy provides an additional check against event queue
        if packet_queue.is_not_empty() and self.is_not_busy():
           
            # dequeue the next packet, set fields, schedule completion
            # service completion time is encoded in the packet
            next_packet = packet_queue.dequeue()
            self.set_packet(next_packet)
            self.schedule_service_completion(next_packet, event_queue)
        
        # if empty, do nothing; there is nothing to do

    def schedule_service_completion(self, packet, event_queue):
        new_event = create_new_event(packet, SERVICE_COMPLETE)
        event_queue.enqueue(new_event)

def create_new_engine():
    new_engine = Engine()
    return new_engine
