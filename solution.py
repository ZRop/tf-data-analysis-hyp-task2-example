import numpy as np
import plotly.graph_objects as go
import warnings
import pandas as pd

from hyppo.ksample import Energy, MMD, DISCO
from scipy.stats import anderson_ksamp
from statsmodels.stats.weightstats import ztest
from statsmodels.distributions.empirical_distribution import ECDF


chat_id = 672508499 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    if anderson_ksamp([x, y]).significance_level < 0.1:
        return False
    else:
        return True
