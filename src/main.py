import pandas as pd
import pyfolio as pf
import matplotlib as plt
%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

returns = pf.utils.get_symbols_rets('FB')
