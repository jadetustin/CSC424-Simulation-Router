from auxiliary import *
from constants import *
from packet import *
from event import *
import queue
import sys
from time import sleep

class EventQueue:

    def __init__(self):

        # again reusing libraries; this time, the PriorityQueue class
        self.internalQueue = queue.PriorityQueue()

    def enqueue(self, event):

        # mark that an event has entered and place it in the queue
        self.internalQueue.put(event.eventData)

    def dequeue(self):

        # remove the next packet from the queue and return
        # other functions are responsible for not calling this when empty
        next_event = self.internalQueue.get()
        return next_event

    def is_empty(self):
        status = self.internalQueue.empty()
        return status

    def handle_arriving_packet(self, gaussian, exponential, 
            event, packet_queue, data_module):
        
        # get the packet
        # also get the effective start time and expected timing
        # we will use this to simulate the processing time
        event_packet = get_packet(event)
        event_expected_time = get_timing(event)
        event_start_marker = get_start_marker(event)
        simulate_processing_time(event_start_marker, event_expected_time)

        # get packet ID and print out that the packet has arrived 
        event_packetID = event_packet.get_packetID()
        print("Packet " + str(event_packetID) + " arrived at router.")
        
        # packet was initialized to random size already
        # as such, just enqueue to the packet queue
        packet_queue.enqueue(event_packet, data_module)
       
       # schedule the next packet
        self.schedule_next_packet(gaussian, exponential)

    def handle_service_completion(self, event, engine, 
            packet_queue, data_module):

        # again get the packet, time it entered the queue, and expected time
        # simulate processing time if needed
        event_packet = get_packet(event)
        event_expected_time = get_timing(event)
        event_start_marker = get_start_marker(event)
        simulate_processing_time(event_start_marker, event_expected_time)

        # get the packet ID and print out that the packet was processed
        event_packetID = event_packet.get_packetID()
        print("Packet " + str(event_packetID) + " sent.")

        # send the packet to the data module so it can update itself
        data_module.validate_packet_data(event_packet)

        # clear the busy marker on the engine and update states
        # this will trigger the engine to process the next packet
        engine.clear_busy(data_module)

    def schedule_next_packet(self, gaussian, exponential):

        # create a new packet first
        # then, create the event
        new_packet = create_new_packet(gaussian, exponential)
        new_event = create_new_event(new_packet, PACKET_ARRIVING) 

        # add to the queue
        self.enqueue(new_event)

def create_new_event_queue():
    new_event_queue = EventQueue()
    return new_event_queue

def simulate_processing_time(start_marker, expected_time):

    # find the amount of time that has passed since being queued
    current_waiting_time = get_timespan(start_marker)
    time_left = expected_time - current_waiting_time

    # if time left in processing is greater than 0, simulate the remaining wait
    if time_left > 0:
        sleep(time_left)
