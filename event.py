from packet import *
from constants import *
from time import time

class Event:

    def __init__(self, packet, event_type):

        # get the timing of the packet
        # varies based on event type
        if event_type is PACKET_ARRIVING:
            timing = packet.get_arrivalTime()
        if event_type is SERVICE_COMPLETE:
            timing = packet.get_processingTime()

        # configure eventData field
        # format is timing, type, packet, stamp
        current_time = time()
        self.eventData = (timing, event_type, packet, current_time)

def create_new_event(packet, event_type):

    # provided for encapsulation purposes; makes for cleaner code
    new_event = Event(packet, event_type)
    return new_event

def get_timing(event_data):
    result = event_data[0]
    return result

def get_event_type(event_data):
    result = event_data[1]
    return result

def get_packet(event_data):
    result = event_data[2]
    return result

def get_start_marker(event_data):
    result = event_data[3]
    return result
