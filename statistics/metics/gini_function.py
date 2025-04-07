from sklearn.metrics import roc_auc_score


# Gini=2×AUC−1
# AUC is 0.85:
# Gini=2×0.85−1=0.70
# It's easily interpreted as a percentage
def gini(y_true, y_scores):
    auc = roc_auc_score(y_true, y_scores)
    return 2 * auc - 1