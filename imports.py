import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
import xlrd
import scipy
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
base = importr('base')
from rpy2.robjects import FloatVector
crank = importr('crank')
npsm = importr('npsm')
