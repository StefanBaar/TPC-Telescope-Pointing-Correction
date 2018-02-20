### pointing script: determine Pointing parameters
### Version 0.2
### Created 2018 02 09:
### by Stefan Baar - stefan.baar87@gmail.com
### last edited (date, name)
### 2018 02 09 - S. Baar


import numpy as np
from bin.io import read_file
from bin.Pfunctions import compute_off, compute_parameters


OPARA = "New_Parameters"
PARA  = "p_parameters.txt"  ### parameters used during data apprehension
FILE  = "examples/20130202.txt"     ### offset data


RADEC, dRADEC, PHI = read_file(FILE)

if para == "":
    PARAMETERS         = np.genfromtxt(PARA)
    ddRADEC            = compute_off(RADEC[:,0], RADEC[:,0],  PHI, param)
    dRADEC             = dRADEC - ddRADEC
else:
    pass


newPARAMETERS = compute_parameters(RADEC, dRADEC, learning_rate = 0.003, maxdW = 0.001)
print "Newly computed pointing parameters:"
print newPARAMETERS

np.savetxt(np.round(newPARAMETERS[0][-1]*3600.,2),　OPARA)
