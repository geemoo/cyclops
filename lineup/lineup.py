#!/usr/bin/env python

from rfsim.models import Lineup
from rfsim.parts.generic import DCBlock
from rfswitches import HMC1118

# create the lineup object
lineup = Lineup()

# add DC block
lineup.add(DCBlock(0.5))

# add tx/rx switch
lineup.add(HMC1118())

# print out the gain of the entire lineup
print "gain = %0.2f dBm" % lineup.gain()
