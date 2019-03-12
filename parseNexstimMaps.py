import numpy as np
import re

def readNexstimMap(filenames, iDep, iChan):
# read TMS mapping data from a Nexstim text file(s)
# filenames - full path(s) to the file(s) containing the data about a single map (may be separated into .._BELOW and .._ABOVE files)
# iDep - index of the used peeling depth (among the depths existing in the file, starting from 0)
# iChan - number of the EMG channel of interest, as in the text file
    trialLines = []
    for i,fn in enumerate(filenames):
        with open(fn) as f:
            lines = f.readlines()
            if i == 0:
                depths = np.array([float(line.split()[2]) for line in lines if 'Peeling depth' in line])
                nDepths = len(depths)
            arr = np.array([line for line in lines if 'ID(' in line])
            trialLines.extend(np.split(arr,nDepths)[iDep])    
    ordering = np.argsort([int(x.split('.')[2]) for x in trialLines])
    trialLines = np.array(trialLines)[ordering]
    nTrials = len(trialLines)    
    loc = np.zeros((nTrials, 3))
    for iTrial, line in enumerate(trialLines):
        loc[iTrial] = np.array([float(x) for x in re.findall('[-+]?[0-9]*\.?[0-9]+', line[line.find('MRI coord'):])])
    iChan = 1
    ampl = np.zeros(nTrials)
    for iTrial, line in enumerate(trialLines):
        chanStr = line.split('EMG%d('%iChan)[1]
        chanStr = chanStr[:chanStr.find(')')]
        numberStrings = re.findall('[-+]?[0-9]*\.?[0-9]+', chanStr)
        if len(numberStrings) < 2:
            numberStrings = ['0', '0']
        ampl[iTrial] = float(numberStrings[0])
    return [loc, ampl]

def saveMap(mapFile,iSubj,iSess,loc,ampl):
# save TMS mapping data to a csv file
# format: index of subject, index of session, x, y, z (in mm), amplitude (in uV)
# x, y, z - coordinates of the electric field maximum at the selected peeling depth
    nTrials = len(loc)
    np.savetxt(mapFile, np.hstack([np.full((nTrials, 1), iSubj+1), np.full((nTrials, 1), iSess+1), loc,ampl[np.newaxis].T]),
               fmt=['%d','%d','%.1f','%.1f','%.1f','%.1f'],delimiter = ';')

