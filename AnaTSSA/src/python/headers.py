"""
This is the file that contains all the imports.
"""

import ROOT
import datetime
import uproot
import sys
import os
import array
import math
import csv
import time
import multiprocessing
import subprocess
import itertools
import numpy as np
import time
import concurrent.futures
import h5py
from sklearn.model_selection import train_test_split
from math import acos, sqrt, pow
from terminaltables import AsciiTable
from matplotlib import pyplot as plt
from multiprocessing.dummy import freeze_support
from random import randint
from colorama import *
from scipy.interpolate import InterpolatedUnivariateSpline as Spline
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, Matern, RationalQuadratic, ExpSineSquared, DotProduct, WhiteKernel, ConstantKernel as C
from sklearn.preprocessing import StandardScaler, Normalizer