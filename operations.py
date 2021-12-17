import numpy as np
#*****************************************************
#               STANDARD ROUTINES
#*****************************************************
#=====================================================
#-----------------------------------------------------
def concatenate4matrices(a,b,c,d):
    ab = np.concatenate((a,b),axis=1)
    cd = np.concatenate((c,d),axis=1)
    abcd = np.concatenate((ab,cd),axis=0)
    return abcd
#-----------------------------------------------------
def getFigFileName(i):
    if(i<10):
        figFileName = "0000%i" % i
    elif(i<100):
        figFileName = "000%i" % i
    elif(i<1000):
        figFileName = "00%i" % i
    elif(i<10000):
        figFileName = "0%i" % i
    return figFileName
#-----------------------------------------------------