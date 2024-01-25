#!/usr/bin/env python3
import minimalmodbus
import sys

instrument = minimalmodbus.Instrument('COM3', 1, debug=True)  # port name, slave address (in decimal)
instrument.serial.baudrate = 9600;

reg = int(sys.argv[2])
offset = int(sys.argv[1])
# print(reg)

val = 61

# read register
# print(instrument.read_register(reg+offset*0, 0))
print(instrument.write_register(reg+offset*1, val))
# print(instrument.read_register(reg+offset*2, 0))
# print(instrument.read_float(reg+offset*0, byteorder=3))
# print(instrument.read_float(reg+offset*1, byteorder=3))
# print(instrument.read_float(reg+offset*2, byteorder=3))
# print(instrument.read_float(1032+30*0, byteorder=3))
# print(instrument.read_float(1032+30*2, byteorder=3))
