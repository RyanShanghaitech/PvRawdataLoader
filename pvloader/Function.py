from numpy import *

def load(path:str, numScan:int=2, numCh:int=2, numPt:int=2, dtype:type=int32) -> ndarray:
    lstRawdata = fromfile("rawdata.job0", dtype=int32)
    lstRawdata = lstRawdata[0::2] + 1j*lstRawdata[1::2] # seperate real and imaginary parts
    lstRawdata = lstRawdata.reshape([numScan, numCh, numPt]).transpose([0,1,2])
    return lstRawdata