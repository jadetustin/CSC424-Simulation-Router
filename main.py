# defined, constant variables and non-object utility functions
from constants import *
from auxiliary import *

# packages created for every object in the system
from packet import *
from packet_queue import *
from event import *
from event_queue import *
from engine import *
from data_collection import *

if __name__ == "__main__":

    # initialize the primary objects
    dm = create_new_data_module()
    e = create_new_engine()
    pq = create_new_packet_queue()
    eq = create_new_event_queue()

    # initialize the randomizers
    rs = seed_randomizers()
    rg = rs[0]
    re = rs[1]

    # run router simulation until sufficient number of packets operated on

    while dm.not_done():
        
        if eq.is_empty():
            eq.schedule_next_packet(rg, re)
            
        else:
            current_event = eq.dequeue()
            event_type = get_event_type(current_event) 

            if event_type == PACKET_ARRIVING:
                eq.handle_arriving_packet(rg, re, current_event, pq, dm)

            if event_type == SERVICE_COMPLETE:
                eq.handle_service_completion(current_event, e, pq, dm)

            if e.is_not_busy():
                e.service_next_packet(pq, eq)

    e.clear_busy(dm)
    dm.finalize_data()
    dm.display_results()

