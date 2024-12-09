from constants import *
import random
import os
from time import time

current_packetID = STARTING_ID

def get_timespan(starting_time):
    current_time = time()
    timespan = current_time - starting_time
    return timespan

def seed_randomizers():

    # configure exponential randomizer first
    exponential = random.Random()
    exponential.seed(os.urandom(4))

    # next, configure gaussian randomizer
    gaussian = random.Random()
    gaussian.seed(os.urandom(4))

    # package them up as a tuple and return it
    randomizers = (gaussian, exponential)
    return randomizers

def get_random_packet_size(gaussian):

    # expects preconfigured randomizer as argument
    packet_size = round(gaussian.gauss(MU, SIGMA))
    if packet_size < MINIMUM_PACKET_SIZE or packet_size > MAXIMUM_PACKET_SIZE:
        packet_size = get_random_packet_size(gaussian)
    return packet_size

def get_random_arrival_time(exponential):

    # expects preconfigured randomizer as argument
    arrival_time = exponential.expovariate(LAMBDA)
    return arrival_time
