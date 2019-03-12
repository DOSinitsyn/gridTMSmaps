from imports import *
from utils import *

def pAndStatGehanR(arr1, arr2):   # supposes that censored values are passed as 0 (left censoring)
# compute the p-value and statistic of Gehan's generalization of the Mann-Whitney test for censored data
# we use the implementation in the R language (npsm package) through the rpy2 interface between R and Python
	uncens = np.concatenate((arr1 != 50, arr2 != 50)).astype(float)
	allData = np.concatenate((-arr1,-arr2))
	groups = np.concatenate((np.zeros(len(arr1)),np.ones(len(arr2))))
	res = robjects.r['gehan.test'](robjects.FloatVector(allData), robjects.FloatVector(uncens), robjects.FloatVector(groups))
	return np.array([res[1][0],res[0][0]])

def ICConeWay(x):   # rows are subjects, columns are repeated tests
# intraclass correlation coefficient corresponding to the one-way ANOVA model
    x = np.array(x)
    nA = len(x); nB = len(x[0]); nAB = nA*nB;
    MA = np.mean(x, axis = 1)
    MB = np.mean(x, axis = 0)
    M = np.mean(x)
    MSA = (nB/(nA-1)) * np.sum((MA - M)**2)
    MSW = (1/(nA*(nB-1))) * np.sum([np.sum((x[i,:] - MA[i])**2) for i in range(nA)])
    return (MSA - MSW) / (MSA + (nB-1) * MSW)

def overlap(arr1,arr2):  # ! only works for samples that are multiples of 0.1
# overlap of the empirical distributions computed from two samples
# the overlap is defined as the integral of the minimum of the two probability densities 
    arr1 = np.round(arr1,1)
    arr2 = np.round(arr2,1)
    c1 = Counter(arr1); c2 = Counter(arr2)
    paramGrid = np.round(np.arange(0,max(max(arr1),max(arr2))+0.1,0.1),1)
    return sum([min(c1[x]/len(arr1),c2[x]/len(arr2)) for x in paramGrid])
        