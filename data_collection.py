from constants import *
from auxiliary import *
from time import time

class DataCollection:

    def __init__(self):

        self.startTime = time()

        # updated using validate_max_queue(size)
        self.maxQueueLength = 0

        # updated using validate_packet_data(packet)
        self.longestWait = 0
        self.totalWait = 0
        self.packetsServiced = 0
        self.dataServiced = 0

        # updated using validate_engine_usage(busy_start)
        self.engineUsage = 0

        # calculated at the end of the program's runtime using finalize_data()
        self.runTime = None
        self.averageWait = None

    def not_done(self):
        if self.packetsServiced < PACKET_THRESHOLD:
            return True
        return False

    def validate_max_queue(self, size):
        if size > self.maxQueueLength:
            self.maxQueueLength = size

    def validate_packet_data(self, packet):

        # get the size of the packet and update packetsServiced, dataServiced
        packet_size = packet.get_packetSize()
        self.packetsServiced += 1
        self.dataServiced += packet_size

        # get the packet's waitStart and obtain the wait time
        packet_waitStart = packet.get_waitStart()
        wait_time = get_timespan(packet_waitStart)

        # update longestWait (conditionally) and totalWait
        self.totalWait += wait_time
        if wait_time > self.longestWait:
            self.longestWait = wait_time

    def validate_engine_usage(self, busy_start):
        busy_time = get_timespan(busy_start)
        self.engineUsage += busy_time

    def finalize_data(self):
        self.averageWait = (self.totalWait / self.packetsServiced)
        self.runTime = get_timespan(self.startTime)

    def display_results(self):

        print("Simulation complete.")
        print("Total uptime: " + str(self.runTime) + " seconds.")
        print("Total number of packets sent: " + str(self.packetsServiced) + ".")
        print("Total data sent: " + str(self.dataServiced) + " bytes.")
        print("Maximum number of packets waiting to be sent: " + 
                str(self.maxQueueLength) + ".")
        print("Longest wait time for a packet: " + 
                str(self.longestWait) + " seconds.")
        print("Average wait time for a packet: " + 
                str(self.averageWait) + " seconds.")
        print("Total engine uptime: " + str(self.engineUsage) + " seconds.")

def create_new_data_module():
    new_module = DataCollection()
    return new_module
