import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import pandas as pd

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'panda_function']

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def rand_array(shape):
    return np.random.rand(*shape)

def my_mat_solve(A, b):
    return A.inv()*b

def panda_function(integer):
    return pd.Series([1, 3, 5, integer, 6, 8])
