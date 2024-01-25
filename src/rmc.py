import subprocess as sp
import msvcrt, time
import lowLevelSerial as llSerial
import rmc_output as output

class AnalogInput:
    def __init__(self):
        self.available = 1
        self.reading = 0
        self.status = 0
        self.calibrationOffset = 0


# Front Panel Input Blocks
inputBlocks = ["A", "B", "D", "E"]

# analog input
ain = []
ain.append({"Range":[{"range":[-1999.000,9999.000]},{"units":"F"}]})
ain.append({"Map1":[360,360+90],"Map2":[420,420+100]})

# input error
ier = []
ier.append({"Range":[{"range":[  {"None":61},
                        {"Open":65},
                        {"Shorted":127},
                        {"Measurement Error":140},
                        {"Bad Calibration Data":139},
                        {"Ambient Error":9},
                        {"RTD Error":141},
                        {"Fail":32}]},{"units":"N/A"}]})
ier.append({"Map1":[362,362+90],"Map2":[422,422+100]})

# calibration offset
ica = []
ica.append({"Range":[{"range":[-1999.00,9999.00]},{"units":"F"}]})
ica.append({"Map1":[382,382+90],"Map2":[442,442+100]})
# print(ain[0]["Map1"][0])

# sensor type
sen = []
sen.append({"Range":[{"range":[  {"Off":62},
                        {"Thermocouple":95},
                        {"Millivolts":56},
                        {"Volts DC":104},
                        {"Milliamps DC":112},
                        {"RTD 100 Ohm":113},
                        {"RTD 1K Ohm":114},
                        {"Potentiometer 1K Ohm":155},
                        {"Thermistor":229}]},{"units":"N/A"}]})
sen.append({"Map1":[368,368+90],"Map2":[428,428+100]})

# sensor TC linearization
tcLin = []
tcLin.append({"Range":[{"range":[  {"B":11},
                        {"C":15},
                        {"D":23},
                        {"E":26},
                        {"F":30},
                        {"J":46},
                        {"K":48},
                        {"N":58},
                        {"R":80},
                        {"S":84},
                        {"T":93}]},{"units":"N/A"}]})
tcLin.append({"Map1":[370,370+90],"Map2":[430,430+100]})

# sensor unit
sUnit = []
sUnit.append({"Range":[{"range":[  {"Absolute Temperature":1540},
                        {"Relative Humidity":1538},
                        {"Process":75},
                        {"Power":73}]},{"units":"N/A"}]})
sUnit.append({"Map1":[442,442+90],"Map2":[502,502+100]})

# control loop set-point
# NOTE: range is not actuall correct. It should be from Low set-Point to Maximum Set Point (per documentation)
cSP = []
cSP.append({"Range":[{"range":[-1999.00,9999.00]},{"units":"F"}]})
cSP.append({"Map1":[2500,2500+80],"Map2":[3340,3340+80]})

# control loop output power
cOP = []
cOP.append({"Range":[{"range":[-100.00,100.00]},{"units":"%"}]})
cOP.append({"Map1":[2248,2248+70],"Map2":[3088,3088+70]})

#### MONITOR MENU ########################3333

# control mode active
cMA = []
cMA.append({"Range":[{"range":[  {"Off":62},
                        {"Auto":10},
                        {"Manual":54}]},{"units":"N/A"}]})
cMA.append({"Map1":[2222,2222+70],"Map2":[3062,3062+70]})

# heat power
hPr = []
hPr.append({"Range":[{"range":[0.00,100.00]},{"units":"%"}]})
hPr.append({"Map1":[2244,2244+70],"Map2":[3084,3084+70]})

# cool power
cPr = []
cPr.append({"Range":[{"range":[-100.00,0.00]},{"units":"%"}]})
cPr.append({"Map1":[2246,2246+70],"Map2":[3086,3086+70]})

### END MONITOR MENU ######################

# low limit set point
lLSP = []
lLSP.append({"Range":[{"range":[-1999.00,9999.00]},{"units":"F"}]})
lLSP.append({"Map1":[724,724+30],"Map2":[824,824+60]})

# high limit set point
hLSP = []
hLSP.append({"Range":[{"range":[-1999.00,9999.00]},{"units":"F"}]})
hLSP.append({"Map1":[726,726+30],"Map2":[826,826+60]})

# limit state
limState = []
limState.append({"Range":[{"range":[  {"Off":62},
                        {"None":61},
                        {"Limit High":51},
                        {"Limit Low":52},
                        {"Error":28}]},{"units":"N/A"}]})
limState.append({"Map1":[730,730+30],"Map2":[830,830+60]})

# clear limit (just writable)
lCr = []
lCr.append({"Range":[{"range":[  {"Clear":0},
                        {"No Change":255}]},{"units":"N/A"}]})
lCr.append({"Map1":[720,720+30],"Map2":[820,820+60]})

# limit status
lSt = []
lSt.append({"Range":[{"range":[  {"Fail":32},
                        {"Safe":1667}]},{"units":"N/A"}]})
lSt.append({"Map1":[744,744+30],"Map2":[844,844+60]})

def readAnalogIn(instrument):
    return llSerial.readMaps_float(instrument,ain[1])


def readCalibrationOffset(instrument):
    return llSerial.readMaps_float(instrument,ica[1])


def readInputErrors(instrument):
    ret = llSerial.readMaps_uint(instrument, ier[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, ier[0])])
    return ret1


def readSensorTypes(instrument):
    ret = llSerial.readMaps_uint(instrument, sen[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, sen[0])])
    return ret1


def readTCLinearization(instrument):
    ret = llSerial.readMaps_uint(instrument, tcLin[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, tcLin[0])])
    return ret1


def readUnits(instrument):
    ret = llSerial.readMaps_uint(instrument, sUnit[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, sUnit[0])])
    return ret1


def readOutputState(instrument):
    ret = llSerial.readMaps_uint(instrument, doS[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, doS[0])])
    return ret1


def readSetPoint(instrument):
    return llSerial.readMaps_float(instrument, cSP[1])


def writeSetPoint(instrument, key, selector, newSP):
    llSerial.writeMaps_float(instrument, cSP[1], key, selector, newSP)


def readOutputPower(instrument):
    return llSerial.readMaps_float(instrument, cOP[1])


def readHeatPower(instrument):
    return llSerial.readMaps_float(instrument, hPr[1])


def readControlMode(instrument):
    ret = llSerial.readMaps_uint(instrument, cMA[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, cMA[0])])
    return ret1


def readCoolPower(instrument):
    return llSerial.readMaps_float(instrument, cPr[1])


def readLowLimitSetPoint(instrument):
    return llSerial.readMaps_float(instrument, lLSP[1])


def readHighLimitSetPoint(instrument):
    return llSerial.readMaps_float(instrument, hLSP[1])


def readLimitState(instrument):
    ret = llSerial.readMaps_uint(instrument, limState[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, limState[0])])
    return ret1


def readLimitStatus(instrument):
    ret = llSerial.readMaps_uint(instrument, lSt[1])
    ret1 = []
    for code in ret:
        ret1.append([code,llSerial.lookupCode(code, lSt[0])])
    return ret1


def getUserInput():
    invalidInput = True
    while invalidInput:
        block = input("Enter input (A, B, D, E): ")
        if block != "A" and block != "B" and block != "D" and block != "E":
            print("You must enter \"A\", \"B\", \"D\", or \"E\" (case sensitive)")
        else:
            invalidInput = False

    if block == "A" or block == "B":
        key = "Map1"
        if block == "A":
            selector = 0
        else:
            selector = 1
    else:
        key = "Map2"
        if block == "D":
            selector = 0
        else:
            selector = 1

    return [block, key, selector]

def PrintLimits(instrument):
    lowLimitSP = readLowLimitSetPoint(instrument)
    highLimitSP = readHighLimitSetPoint(instrument)
    limitState = readLimitState(instrument)
    limitStatus = readLimitStatus(instrument)
    tmp = sp.call('cls',shell=True)
    print("Input\tLow Lim. SP ("+lLSP[0]["Range"][1]["units"]+")\tHigh Lim. SP ("+hLSP[0]["Range"][1]["units"]+")\tLim. State\tLim. Status")
    for i in range(len(inputBlocks)):
        print("{0:<2s}\t{1:5.2f}\t\t{2:5.2f}\t\t\t{3:<16s}{4:<22s}".format(inputBlocks[i],lowLimitSP[i],highLimitSP[i],limitState[i][1],limitStatus[i][1]))


def PrintMonitorMenu(instrument):
    controlMode = readControlMode(instrument)
    heatPower = readHeatPower(instrument)
    coolPower = readCoolPower(instrument)
    tmp = sp.call('cls',shell=True)
    print("Input\tControl Mode\t\tHeat Power ("+hPr[0]["Range"][1]["units"]+")\tCool Power ("+cPr[0]["Range"][1]["units"]+")")
    for i in range(len(inputBlocks)):
        print("{0:<2s}\t{1:<22s}\t{2:4.2f}\t\t{3:4.2f}".format(inputBlocks[i],controlMode[i][1],heatPower[i],coolPower[i]))


def PrintAnalogInputStatus(instrument):
    # print(ain[0]["Range"][1])
    exit = False
    while exit != True:
        analogIn = readAnalogIn(instrument)
        calOff = readCalibrationOffset(instrument)
        stat = readInputErrors(instrument)
        # dummy variable tmp to eliminate a "0" from showing up
        tmp = sp.call('cls',shell=True)
        print("Press x to exit")
        print("Input\tReading ("+ain[0]["Range"][1]["units"]+")\t Error\t\t\tCal. Offset ("+ica[0]["Range"][1]["units"]+")")
        for i in range(len(inputBlocks)):
            # print("{0:<2s}\t{1:5.2f}\t\t{2:3d}\t{3:5.2f}".format(inputBlocks[i],analogIn[i],stat[i],calOff[i]))
            print("{0:<2s}\t{1:5.2f}\t\t{2:<22s}\t{3:5.2f}".format(inputBlocks[i],analogIn[i],stat[i][1],calOff[i]))

        time.sleep(0.3)
        if msvcrt.kbhit():
            key = str(msvcrt.getch())
            # print(key)
            # print(len(key))
            # print(type(key))
            if key == "b\'x\'":
                exit = True


def PrintAnalogInputSettings(instrument):
    sensorTypes = readSensorTypes(instrument)
    sensorLinearization = readTCLinearization(instrument)
    units = readUnits(instrument)
    tmp = sp.call('cls',shell=True)
    print("Input\tSensor Type\t\tTC Linearization (Type)\tSensor Units")
    for i in range(len(inputBlocks)):
        print("{0:<2s}\t{1:<22s}\t{2:<22s}\t{3:<22s}".format(inputBlocks[i],sensorTypes[i][1],sensorLinearization[i][1],units[i][1]))


def IOstatus(instrument):
    exit = False
    while exit != True:
        processValue = readAnalogIn(instrument)
        setpoint = readSetPoint(instrument)
        output = readOutputPower(instrument)
        tmp = sp.call('cls',shell=True)
        print("Press x to exit")
        print("Input\tPV ("+ain[0]["Range"][1]["units"]+")\t\tSP ("+cSP[0]["Range"][1]["units"]+")\tOutput State ("+cOP[0]["Range"][1]["units"]+")")
        for i in range(len(inputBlocks)):
            # print("{0:<2s}\t{1:5.2f}\t\t{2:5.2f}\t{3:<4s}".format(inputBlocks[i],processValue[i],setpoint[i],output[i][1]))
            print("{0:<2s}\t{1:5.2f}\t\t{2:5.2f}\t{3:<4.2f}".format(inputBlocks[i],processValue[i],setpoint[i],output[i]))

        time.sleep(0.3)
        if msvcrt.kbhit():
            key = str(msvcrt.getch())
            # print(key)
            # print(len(key))
            # print(type(key))
            if key == "b\'x\'":
                exit = True


def SetSP(instrument):
    tmp = sp.call('cls',shell=True)
    print("Current set points")
    setpoint = readSetPoint(instrument)
    print("Input\tSP ("+cSP[0]["Range"][1]["units"]+")")
    for i in range(len(inputBlocks)):
        print("{0:<2s}\t{1:5.2f}".format(inputBlocks[i],setpoint[i]))

    [block, key, selector] = getUserInput()

    newSP = float(input("Enter new setpoint for "+block+": "))

    writeSetPoint(instrument,key,selector,newSP)


def PrintOutputSettings(instrument):
    tmp = sp.call('cls',shell=True)
    print("Input\tOutput Func.\t      Output Type\t    O.P. Func.\t\t   O.P. Scale Low\t O.P. Scale High")

    outputFunction = output.readOutputFunction(instrument)
    outputProcessType = output.readOutputProcessOutputType(instrument)
    outputProcessFunction = output.readOutputProcessFunction(instrument)
    outputProcessScaleLow = output.readOutputProcessScaleLow(instrument)
    outputProcessScaleHigh = output.readOutputProcessScaleHigh(instrument)
    for i in range(len(inputBlocks)):
        print("{0:<2s}\t{1:<22s}{2:<22s}{3:<22s}{4:5.2f}\t\t\t{5:5.2f}".format(inputBlocks[i],
        outputFunction[i][1],outputProcessType[i][1],outputProcessFunction[i][1],
        outputProcessScaleLow[i],outputProcessScaleHigh[i]))

    print("Input\t O.P. Range Low\t\t O.P. Range High\t O.P. Cal. Offset")
    outputProcessRangeLow = output.readOutputProcessRangeLow(instrument)
    outputProcessRangeHigh = output.readOutputProcessRangeHigh(instrument)
    outputProcessCalibrationOffset = output.readOutputProcessCalibrationOffset(instrument)
    for i in range(len(inputBlocks)):
        print("{0:<2s}\t{1:5.2f}\t\t\t{2:5.2f}\t\t\t{3:5.2f}".format(inputBlocks[i],
        outputProcessRangeLow[i],outputProcessRangeHigh[i],outputProcessCalibrationOffset[i]))


def SetOutputFunction(instrument):
    tmp = sp.call('cls',shell=True)
    print("Current Output Functions")
    outputFunction = output.readOutputFunction(instrument)
    print("Input\tOutput Function\t\tReg. Value")
    for i in range(len(inputBlocks)):
        print("{0:<2s}\t{1:<22s}\t{2:3d}".format(inputBlocks[i],outputFunction[i][1],outputFunction[i][0]))

    [block, key, selector] = getUserInput()

    print("Output Function Options")
    for i in range(len(output.oFn[0]["Range"][0]["range"])):
        for codeName, codeNumber in output.oFn[0]["Range"][0]["range"][i].items():
            print(str(i)+". "+codeName)

    optionIndex = int(input("Enter new output function option for "+block+": "))

    for codeName, codeNumber in output.oFn[0]["Range"][0]["range"][optionIndex].items():
        value = codeNumber

    output.setOutputFunction(instrument,key,selector,value)


def setControlMode(instrument, key, selector, value):
    llSerial.writeMaps_uint(instrument, cMA[1], key, selector, value)


def SetControlMode(instrument):
    tmp = sp.call('cls',shell=True)
    print("Current Control Mode")
    controlMode = readControlMode(instrument)
    print("Input\tControl Mode\t\tReg. Value")
    for i in range(len(inputBlocks)):
        print("{0:<2s}\t{1:<22s}\t{2:3d}".format(inputBlocks[i],controlMode[i][1],controlMode[i][0]))

    [block, key, selector] = getUserInput()

    print("Control Mode Options")
    for i in range(len(cMA[0]["Range"][0]["range"])):
        for codeName, codeNumber in cMA[0]["Range"][0]["range"][i].items():
            print(str(i)+". "+codeName)

    optionIndex = int(input("Enter new output function option for "+block+": "))

    for codeName, codeNumber in cMA[0]["Range"][0]["range"][optionIndex].items():
        value = codeNumber

    setControlMode(instrument,key,selector,value)
