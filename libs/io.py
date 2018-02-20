##### IO functions for pointing lists
### Version 0.2
### Created 2018 02 09:
### by Stefan Baar - stefan.baar87@gmail.com
### last edited (date, name)
### 2018 02 09 - S. Baar

import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

def name_to_time(file1):
    time = file1[:4]+"-"+file1[4:6]+"-"+file1[6:8]
    return time

def readtxt(fname):
    with open(fname) as f:
        content = f.read().splitlines()
        a = []
        for i in content:
            a.append(i.split())

    return [a[0],np.asarray(a[1:]).astype("float")]


def get_groups(data1):
    obj1RA = data1[:,:3]
    obj1DC = data1[:,3:6]
    tel1RA = data1[:,6:9]
    tel1DC = data1[:,9:12]
    time1  = data1[:,12:]
    return obj1RA,obj1DC,tel1RA,tel1DC,time1

def to_string(data): ### convert coordinate arrays to string
    string = []

    for i in data:
        if i.shape[0] == 3:
            string.append(str(int(i[0]))+":"+str(int(i[1]))+":"+str(i[2]))
        else:
            string.append(str(int(i[0]))+":"+str(int(i[1])))
    return string


def get_coord(RA, DEC):

    COORD = []
    for i in range(RA.shape[0]):
        C = SkyCoord(RA[i]+" "+DEC[i],unit=(u.hourangle, u.deg))
        COORD.append([C.ra.deg,C.dec.deg])
    return np.asarray(COORD)

def center_RA(data): #### limit RA to -180 <= RA <= 180
    for i in range(data.shape[0]):
        if data[i,0] > 180.:
            data[i,0] = data[i,0]-360.
        elif data[i,0] < -180.:
            data[i,0] = data[i,0]+360.
        else:
            pass
    return data

##### equatorial telescope coordinates (RA - sideral TIME, DEC )
def read_file(file1, phi = "+35:01:32.0"):
    content0 = readtxt(file1)
    floatsar = get_groups(content0[1])
    RA   = np.asarray(to_string(floatsar[0]))
    DEC  = np.asarray(to_string(floatsar[1]))
    dRA  = np.asarray(to_string(floatsar[2]))
    dDEC = np.asarray(to_string(floatsar[3]))

    PHI  = np.chararray(RA.shape, itemsize=9)
    PHI[:]  = phi
    PHI  = np.asarray(PHI)
    TIME = np.asarray(to_string(floatsar[4]))

    RADEC  = get_coord(RA  ,DEC)
    dRADEC = get_coord(dRA ,dDEC)
    TIMEPHI= get_coord(TIME, PHI)
    phiNUM = TIMEPHI[:,1].copy()
    TIMEPHI[:,1] = 0

    RADEC  = center_RA(RADEC  - TIMEPHI)
    dRADEC = center_RA(dRADEC - TIMEPHI)

    return RADEC, dRADEC, phiNUM
