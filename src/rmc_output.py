import lowLevelSerial as llSerial

# output function
oFn = []
oFn.append({"Range":[{"range":[  {"Off":62},
                        {"Analog Input":142},
                        {"Alarm":6},
                        {"Cool Power":161},
                        {"Heat Power":160},
                        {"Compare":230},
                        {"Counter":231},
                        {"Digital I/O":1142},
                        {"Profile Event Out A":233},
                        {"Profile Event Out B":234},
                        {"Profile Event Out C":235},
                        {"Profile Event Out D":236},
                        {"Profile Event Out E":247},
                        {"Profile Event Out F":248},
                        {"Profile Event Out G":249},
                        {"Profile Event Out H":250},
                        {"Function Key":1001},
                        {"Logic":239},
                        {"Linearization":238},
                        {"Math":240},
                        {"Process Value":241},
                        {"Spec. Func. Output 1":1532},
                        {"Spec. Func. Output 2":1533},
                        {"Spec. Func. Output 3":1534},
                        {"Spec. Func. Output 4":1535},
                        {"Timer":244},
                        {"Variable":245},
                        {"Heater Error":184}]},{"units":"N/A"}]})
oFn.append({"Map1":[1028,1028+30*2],"Map2":[1548,1548+40]})

# Output Digital: Output Function Instance
odOFI = []
odOFI.append({"Range":[{"range":[1,250]},{"units":"N/A"}]})
odOFI.append({"Map1":[1030,1030+30*2],"Map2":[1550,1550+40]})

# Output Digital: Output Source Zone
odOSZ = []
odOSZ.append({"Range":[{"range":[0,24]},{"units":"N/A"}]})
odOSZ.append({"Map1":[1042,1042+30*2],"Map2":[1562,1562+40]})

# Output Digital: Time Base Type
odTBT = []
odTBT.append({"Range":[{"range":[  {"Fixed Time Base":34},
                        {"Variable Time Base":103}]},{"units":"N/A"}]})
odTBT.append({"Map1":[1022,1022+30],"Map2":[1542,1542+40]})

# Output Digital: Fixed Time Base
odFTB = []
odFTB.append({"Range":[{"range":[0.1,60.0]},{"units":"s"}]})
odFTB.append({"Map1":[1024,1024+30],"Map2":[1544,1544+40]})

# Output Digital: Low Power Scale
odLPS = []
odLPS.append({"Range":[{"range":[0.0,100]},{"units":"%"}]})
odLPS.append({"Map1":[1036,1036+30],"Map2":[1556,1556+40]})

# Output Digital: High Power Scale
odHPS = []
odHPS.append({"Range":[{"range":[0.0,100]},{"units":"%"}]})
odHPS.append({"Map1":[1038,1038+30],"Map2":[1558,1558+40]})

# Output Digital: Output State
odOS = []
odOS.append({"Range":[{"range":[  {"Off":62},
                        {"On":63}]},{"units":"N/A"}]})
odOS.append({"Map1":[1032,1032+30],"Map2":[1552,1552+40]})

# Output Digital: Output Source Value
# Refer to documentation for actual limits
odOSV = []
odOSV.append({"Range":[{"range":[-1999.00,9999.00]},{"units":"N/A"}]})
odOSV.append({"Map1":[1044,1044+30],"Map2":[1564,1564+40]})

# Output Process: Output Type
opOT = []
opOT.append({"Range":[{"range":[  {"Volts":104},
                        {"Milliamps":112}]},{"units":"N/A"}]})
opOT.append({"Map1":[840,840+48],"Map2":[1060,1060+120]})

# Output Process: Function
opFn = []
opFn.append({"Range":[{"range":[  {"Off":62},
                        {"Analog Input":142},
                        {"Current":22},
                        {"Cool Power":161},
                        {"Heat Power":160},
                        {"Power":73},
                        {"Linearization":238},
                        {"Math":240},
                        {"Process Value":241},
                        {"Set Point Closed":242},
                        {"Set Point Open":243},
                        {"Spec. Func. Output 1":1532},
                        {"Spec. Func. Output 2":1533},
                        {"Spec. Func. Output 3":1534},
                        {"Spec. Func. Output 4":1535},
                        {"Variable":245},
                        {"Wattage":1697},
                        {"Load Voltage":1698},
                        {"Load Resistance":1183}]},{"units":"N/A"}]})
opFn.append({"Map1":[842,842+48],"Map2":[1062,1062+120]})

# Output Process: Output Function Instance
opOFI = []
opOFI.append({"Range":[{"range":[1,250]},{"units":"N/A"}]})
opOFI.append({"Map1":[846,846+48],"Map2":[1066,1066+120]})

# Output Process: Output Source Zone
opOSZ = []
opOSZ.append({"Range":[{"range":[0,24]},{"units":"N/A"}]})
opOSZ.append({"Map1":[],"Map2":[1096,1096+120]})

# Output Process: Scale Low
opSL = []
opSL.append({"Range":[{"range":[-100.0,100.0]},{"units":"N/A"}]})
opSL.append({"Map1":[856,856+48],"Map2":[1076,1076+120]})

# Output Process: Scale High
opSH = []
opSH.append({"Range":[{"range":[-100.0,100.0]},{"units":"N/A"}]})
opSH.append({"Map1":[858,858+48],"Map2":[1078,1078+120]})

# Output Process: Range Low
opRL = []
opRL.append({"Range":[{"range":[-1999.00,9999.00]},{"units":"F"}]})
opRL.append({"Map1":[860,860+48],"Map2":[1080,1080+120]})

# Output Process: Range High
opRH = []
opRH.append({"Range":[{"range":[-1999.00,9999.00]},{"units":"F"}]})
opRH.append({"Map1":[862,862+48],"Map2":[1082,1082+120]})

# Output Process: Calibration Offset
opCO = []
opCO.append({"Range":[{"range":[-1999.00,9999.00]},{"units":"F"}]})
opCO.append({"Map1":[852,852+48],"Map2":[1072,1072+120]})

# Output Process: Analog Source Value
opASV = []
opASV.append({"Range":[{"range":[-1999.00,9999.00]},{"units":"F"}]})
opASV.append({"Map1":[],"Map2":[1092,1092+120]})

# Output Process: Analog Output Value
opAOV = []
opAOV.append({"Range":[{"range":[0,20.00]},{"units":"F"}]})
opAOV.append({"Map1":[],"Map2":[1090,1090+120]})

def readOutputFunction(instrument):
    ret = llSerial.readMaps_uint(instrument, oFn[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, oFn[0])])
    return ret1


def readOutputProcessOutputType(instrument):
    ret = llSerial.readMaps_uint(instrument, opOT[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, opOT[0])])
    return ret1


def readOutputProcessFunction(instrument):
    ret = llSerial.readMaps_uint(instrument, opFn[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, opFn[0])])
    return ret1


def setOutputFunction(instrument, key, selector, value):
    llSerial.writeMaps_uint(instrument, oFn[1], key, selector, value)


def readOutputProcessOutputFunctionInstance(instrument):
    return llSerial.readMaps_uint(instrument, opOFI[1])


def readOutputProcessOutputSourceZone(instrument):
    return llSerial.readMaps_uint(instrument, opOSZ[1])


def readOutputProcessScaleLow(instrument):
    return llSerial.readMaps_float(instrument, opSL[1])


def readOutputProcessScaleHigh(instrument):
    return llSerial.readMaps_float(instrument, opSH[1])


def readOutputProcessRangeLow(instrument):
    return llSerial.readMaps_float(instrument, opRL[1])


def readOutputProcessRangeHigh(instrument):
    return llSerial.readMaps_float(instrument, opRH[1])


def readOutputProcessCalibrationOffset(instrument):
    return llSerial.readMaps_float(instrument, opCO[1])


def readOutputProcessAnalogSourceValue(instrument):
    return llSerial.readMaps_float(instrument, opASV[1])


def readOutputProcessAnalogOutputValue(instrument):
    return llSerial.readMaps_float(instrument, opAOV[1])
