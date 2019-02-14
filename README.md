gas_sensing


Read data from an environmental sensing device

----------------------------------------

Eample output:
minimalmodbus.Instrument<id=0x7f544187ac50, address=247, mode=rtu, close_port_after_each_call=False, precalculate_read_size=True, debug=False, serial=Serial<id=0x7f544187ac18, open=True>(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=2.0, xonxoff=False, rtscts=False, dsrdtr=False)>

Count :  20.7

O2 :  20.9

CH4 :  0.1

CO :  0.0

CO2 :  6553.5

VOC :  6553.5

Humidity :  22.8

Ambient Temperature :  35.7

Barometric Pressure :  100.2

---------- 0 ---------------

Count :  21.3

O2 :  20.9

CH4 :  0.1

CO :  0.0

CO2 :  6553.5

VOC :  6553.5

Humidity :  22.7

Ambient Temperature :  35.7

Barometric Pressure :  100.2

---------- 1 ---------------

----------------------------------------

Instructions:
- After connecting the device, rune "dmesg" in terminal to verify the serial port (here assumed as "/dev/ttyUSB0")
- Ensure permission is enabled: sudo chmod 777 /dev/ttyUSB0
- Execute "m3sh.py"
