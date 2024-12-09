# number of packets that must be serviced before exiting
# set to 100 in debugging; real execution will be at 1000
PACKET_THRESHOLD = 10000

# in bytes per second; equivalent to 100Mbps
THROUGHPUT = 12500000

# used to balance out exponential randomizer, which outputs in microseconds
MICROSECONDS_PER_SECOND = 1000000

# used as the starting point for packet ID numbering
STARTING_ID = 100000

# constants to establish meaning for event classes
SERVICE_COMPLETE = 11
PACKET_ARRIVING = 22

# used for packet arrival randomizer, roughly equals 1 packet per 0.0001 seconds
LAMBDA = 0.01

# used for packet size randomizer
MU = 750
SIGMA = 200

# minimum, maximum packet sizes in bytes
MINIMUM_PACKET_SIZE = 40
MAXIMUM_PACKET_SIZE = 1460
