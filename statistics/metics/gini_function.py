from sklearn.metrics import roc_auc_score


# Gini=2×AUC−1
# AUC is 0.85:
# Gini=2×0.85−1=0.70
# It's easily interpreted as a percentage
def gini(y_true, y_scores):
    auc = roc_auc_score(y_true, y_scores)
    return 2 * auc - 1



# main function
if __name__ == "__main__":
    y_true = [1, 0, 1, 1, 0, 1, 0]
    y_pred = [1, 0, 0, 1, 0, 1, 1]
    result = gini(y_true, y_pred)
    print(f"result: {result}", )