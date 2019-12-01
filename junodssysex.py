#!/usr/bin/python


def checksum(values):
    cs = 0
    for i in range(7, len(values)-2):
        cs += values[i]
    cs = cs % 128
    cs = 128 - cs
    return cs

# 0=patch, 1=perform, 2=GM1, 3=GM2, 4=GS
def soundMode(mode):
    values = [0xF0,
              0x41,
              0x10,
              0x00,
              0x00,
              0x3A,
              0x12, # DT1 (Data Set 1)
              0x01,
              0x00,
              0x00,
              0x00, # Sound Mode
              0x00, # Data: Patch/perform/GM1/GM2/GS
              0x00, # Checksum
              0xF7]

    values[11] = mode
    values[12] = checksum(values)

    return values

# -5 to +6
def transpose(semis):
    values = [0xF0,
              0x41,
              0x10,
              0x00,
              0x00,
              0x3A,
              0x12, # DT1 (Data Set 1)
              0x01,
              0x00,
              0x00,
              0x12, # Transpose
              0x00, # Data: Transpose val (59-70 = -5 to +6)
              0x00, # Checksum,
              0xF7]

    values[11] = 64 + semis
    values[12] = checksum(values)

    return values

def hexString(values):
    s = ''
    for v in values:
        s += '%02X '%v
    s = s.strip()
    return s


print('Sound Mode:')
print('Patch:   %s'%(hexString(soundMode(0))))
print('Perform: %s'%(hexString(soundMode(1))))
print('GM1:     %s'%(hexString(soundMode(2))))
print('GM2:     %s'%(hexString(soundMode(3))))
print('GS:      %s'%(hexString(soundMode(4))))
print('')

print('Transpose:')
for i in range(-5, 7):
    print('Transpose %d: %s'%(i, hexString(transpose(i))))


    
