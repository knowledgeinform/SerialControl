import struct

def readFloat(instrument, m_register):
    res = instrument.read_register(m_register, 0) # low-order bytes
    res2 = instrument.read_register(m_register+1, 0) # high-order bytes
    # print("results")
    # print(hex(res))
    # print(hex(res2))
    res3 = ((res2 << 16) | res)
    # print(hex(res3))
    res4 = struct.unpack('f', struct.pack('I', res3))[0]
    return res4

def readMaps_float(instrument, map):
    # print(map)
    ret = []
    keys = ["Map1","Map2"]
    for key in keys:
        for m_register in map[key]:
            ret.append(readFloat(instrument,m_register))

    return ret

def writeMaps_float(instrument, map, key, selector, value):
    # print(map)
    m_register = map[key][selector]
    instrument.write_float(m_register, value, byteorder=3)


def writeMaps_uint(instrument, map, key, selector, value):
    m_register = map[key][selector]
    instrument.write_register(m_register,value, 0)


def readMaps_uint(instrument, map):
    # print(map)
    ret = []
    keys = ["Map1","Map2"]
    for key in keys:
        for m_register in map[key]:
            ret.append(instrument.read_register(m_register, 0))

    return ret


def lookupCode(code, rangeMap):
    for codeObj in rangeMap["Range"][0]["range"]:
        # print(type(codeObj))
        for codeName, codeNumber in codeObj.items():
            if code == codeNumber:
                # print(codeName)
                return codeName

    return "UNKNOWN"

def returnCode(tag, rangeMap):
    for codeObj in rangeMap["Range"][0]["range"]:
        # print(type(codeObj))
        for codeName, codeNumber in codeObj.items():
            if tag == codeName:
                # print(codeName)
                return codeNumber

    return
