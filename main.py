import numpy as np # linear algebra
import pandas as pd # data processing

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

#import keras
import tensorflow

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import TimeSeriesSplit

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Any results you write to the current directory are saved as output.
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#load the data
data = pd.read_csv('C:/Users/umkarasi/Desktop/vscode/timeseriespower/data/energy_dataset.csv',
                   index_col=0,
                   parse_dates=[0])

print(data.head(1))