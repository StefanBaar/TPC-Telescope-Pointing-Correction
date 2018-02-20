### pointing functions
### Version 0.2
### Created 2018 02 09:
### by Stefan Baar - stefan.baar87@gmail.com
### last edited (date, name)
### 2018 02 09 - S. Baar
import numpy as np

import torch
from torch.autograd import Variable


def compute_M(RA, DEC,  PHI):
    ra, dec, phi = np.asarray([RA, DEC, PHI])*np.pi/180.
    s = ra.shape

    raC = np.asarray([  np.ones(s),                      ##IH
                        np.zeros(s),
                        np.tan(dec),              ##NP
                        1./np.cos(dec),           ##CH
                        np.sin(ra) * np.tan(dec) ,##ME
                        (-1.)*np.cos(ra) * np.tan(dec), ##MA
                        np.zeros(s),
                        (-1.)*(np.cos(phi)*np.cos(ra) + np.sin(phi)*np.tan(dec) ),##FDAF
                        np.sin(ra),                  ##HCES
                        np.cos(ra), ##HCEC
                        np.zeros(s),
                        np.zeros(s),
                        np.sin(ra) * np.tan(dec), ##DNP
                        np.cos(phi) * np.sin(ra) / np.cos(dec)])#, ##TF
                        #np.zeros(s)])

    deC = np.asarray(  [np.zeros(s),
                        np.ones(s), ##ID
                        np.zeros(s),
                        np.zeros(s),
                        np.cos(ra), ##ME
                        np.sin(ra),  ##MA
                        np.cos(ra),  ##FO
                        np.zeros(s),
                        np.zeros(s),
                        np.zeros(s),
                        np.sin(dec), ##DCES
                        np.cos(dec), ##DCEC
                        np.zeros(s),
                        np.cos(phi)*np.cos(ra)*np.sin(dec) - np.sin(phi)*np.cos(dec)])#, ##TF
                        #np.zeros(s)])

    return np.swapaxes(np.asarray([raC, deC]), 1,2)


def compute_parameters(H, D, learning_rate = 0.003, maxdW = 3.):
    ########### variable learning rate not yet implemented
    ########### numpy arrays to torch tensor opperations
    dtype = torch.FloatTensor
    X = Variable(torch.from_numpy(H).type(dtype), requires_grad=False)
    Y = Variable(torch.from_numpy(D.T).type(dtype), requires_grad=False)
    W = Variable(torch.randn(X.shape[-1]).type(dtype), requires_grad=True)

    ########### Logging Lists (only alpha version)
    LOSS  = []
    weight= []
    dweight= []

    MW = 10.
    while MW > maxdW:

        yp   = torch.matmul(X,W)
        loss = (yp - Y).pow(2).sum()                ### compute square loss

        LOSS.append(loss.data[0])

        loss.backward()

        dweight.append(W.grad.data.numpy().copy())  ### logging differential weights
        weight.append(W.data.numpy().copy())        ### logging weights

        W.data -=learning_rate * W.grad.data        ### new weights

        W.grad.data.zero_()                         ### reset wieghts
        MW = np.abs(dweight[-1]).max()
    return np.asarray(weight), np.asarray(dweight), np.asarray(LOSS)
