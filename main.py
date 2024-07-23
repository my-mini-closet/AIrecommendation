import numpy as np
import pandas as pd
import random

import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

import os
import warnings
warnings.filterwarnings('ignore')
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
print('Device:', device)


import config
CONFIG = config.config()

import customdata as cData
cdataset = cData.CustomDataSet()
cdataset.hello()