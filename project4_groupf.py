# -*- coding: utf-8 -*-
"""Project4_GroupF

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1utBQHr_oPlxhJyBFJ8dyVenwWwg_nBRx
"""

import numpy as np
import pandas as pd
import glob

# Call in the needed observed and GFS data

!wget https://raw.githubusercontent.com/swnesbitt/ATMS-597-SP-2020/master/ATMS-597-SP-2020-Project-4/KCMI_daily.csv
!wget https://raw.githubusercontent.com/swnesbitt/ATMS-597-SP-2020/master/ATMS-597-SP-2020-Project-4/KCMI_hourly.csv

path = '/content/drive/My Drive/Colab Notebooks/Project4/daily/bufkit/' # path to the data
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

daily_data = pd.concat(li, axis=0, ignore_index=True)

daily_data

path = '/content/drive/My Drive/Colab Notebooks/Project4/prof/bufkit' # path to the data
all_files = glob.glob(path + "/*.csv")

li_1 = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li_1.append(df)

prof_data = pd.concat(li_1, axis=0, ignore_index=True)
prof_data

path = '/content/drive/My Drive/Colab Notebooks/Project4/sfc/bufkit' # path to the data
all_files = glob.glob(path + "/*.csv")

li_2 = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li_2.append(df)

sfc_data = pd.concat(li_2, axis=0, ignore_index=True)
sfc_data

daily_obs = pd.read_csv('KCMI_daily.csv', header=4, skipfooter=7, error_bad_lines=False, engine='python')
hourly_obs = pd.read_csv('KCMI_hourly.csv')

test = pd.read_csv('/content/drive/My Drive/Colab Notebooks/ATMS_597_Project_4/Profile/2010010112.gfs_kcmi.buf_prof.csv')



