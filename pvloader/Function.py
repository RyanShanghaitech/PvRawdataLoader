from numpy import *

def load(path:str, numScan:int, numCh:int, numPt:int, dtype:type=int32) -> ndarray:
    lstRawdata = fromfile("rawdata.job0", dtype=int32)
    lstRawdata = lstRawdata[0::2] + 1j*lstRawdata[1::2] # seperate real and imaginary parts
    lstRawdata = lstRawdata.reshape([numScan, numCh, numPt])
    return lstRawdata