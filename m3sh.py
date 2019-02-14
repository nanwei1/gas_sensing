#!/home/nan/miniconda3/bin/python

import minimalmodbus
import time

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 247)
print(instrument)
REGISTER_NAME = {  'Count': 22,
                    'O2':   56,
                    'CH4':  57,
                    'CO':   58,
                    'CO2':  155,
                    'VOC':  156,
                    'Humidity':             243,
                    'Ambient Temperature':  244,
                    'Barometric Pressure':  247}
i=0
while True:
    for reading in REGISTER_NAME:
        print(reading, ": ", str(instrument.read_register(REGISTER_NAME[reading],1)))
    print("----------", str(i), "---------------")
    time.sleep(5)
    i+=1

# print(instrument.read_register(56,1))