# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 08:59:27 2025

@author: Olga Ioffe

This is a Python version of standing waves analysis in Matlab
"""

# Import
import numpy as np # vectors and matrices function
import matplotlib.pyplot as plt # plotting figures

# define function for calculating speed of sound in air for given temperature
# input: T [C]
# output v [m/sec]
def vsound_in_air(T):
    
    C2K = 273.15 # Celsius to Kelvin conversion
    v0 = 331.7 # [m/sec] v sound in air at 0[C]

    T0 = C2K # 0 [C] 
    v02 = v0 * v0
    gRbyM = v02 / T0 # gama*R/M

    T1_air = T + C2K # [deg]
    return np.sqrt(gRbyM*T1_air) # [m/sec]


# define function for calculating wavelength of sound in air for given temperature and frequency
# input: freq [Hz], T [C]
# output: lambda [m]
# calling functions: vsound_in_air
def lambda_sound_in_air (freq, T):

    vsound = vsound_in_air(T) #[m/sec]
    return vsound / freq # wavelength in air [m]

T =22
v =  vsound_in_air(T)
print(v)
f = 4000
lam = lambda_sound_in_air (f, T) * 100
print(lam)

