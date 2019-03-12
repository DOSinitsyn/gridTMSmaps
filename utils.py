from imports import *

def setSize(x, y):
    plt.gcf().set_size_inches(x,y)

def norm(vec):
	return np.linalg.norm(vec)
    
def chopSmall(v, thr=50):
# set subthreshold values to zero
    return np.array([x if x >= thr else 0 for x in v])
    
def censorSmall(v, thr=50):
# make subthreshold values equal to the threshold (as assumed by the Gehan test for censored data)
    return np.array([x if x >= thr else thr for x in v])

def flatten2d(arr):
    return np.array([x for line in arr for x in line])

def meanWithoutNAN(arr):
    arr = np.array(arr)
    return np.mean(arr[~np.isnan(arr)])
    
def CV(a):
    return scipy.stats.variation(a)
    