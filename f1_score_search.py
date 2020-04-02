import numpy as np
from sklearn.metrics import f1_score


# 找到f1 score的最佳阈值
def search_threthold(true,pred):
    score = 0
    bestThrethold = 0
    for i in np.arange(0, 1, 0.01):
        cur_score = f1_score(true, np.where(pred > i, 1, 0))
        if cur_score > score:
            score = cur_score
            bestThrethold = i
    return bestThrethold

