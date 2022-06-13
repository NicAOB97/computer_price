import pandas as pd
import numpy as np 
import seaborn as sns
import re

# matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt

import urllib.request
from PIL import Image

from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler