import pandas as pd
import numpy as np


chat_id = 672508499 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    if anderson_ksamp([x, y]).significance_level < 0.1:
        return False
    else:
        return True
