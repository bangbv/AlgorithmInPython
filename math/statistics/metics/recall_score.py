"""
Recall=TP​/(TP+FN)
Intuition: Of all the real positive cases, how many did the model catch?
When To Use:
- Medical diagnosis : Don’t miss sick patients
- Fraud detection : Better to flag suspicious cases
"""

from sklearn.metrics import recall_score

y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1]

recall = recall_score(y_true, y_pred)
print(f"Recall: {recall:.2f}")
