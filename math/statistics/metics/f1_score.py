from sklearn.metrics import f1_score

# The F1 score is the harmonic mean of Precision and Recall.
"""
F1 Score=2×(Precision×Recall / Precision+Recall​)

When to Use
- You care about both false positives and false negatives.
- Your dataset is imbalanced. (e.g., fraud detection, rare disease prediction)
- Accuracy would be misleading.
"""

y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1]

f1 = f1_score(y_true, y_pred)
print(f"F1 Score: {f1:.2f}")