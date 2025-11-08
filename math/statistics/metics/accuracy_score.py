"""
Accuracy=(TP+TN​)/(TP+TN+FP+FN)
Intution: Out of everything the model predicted, how much did it get right?
When To Use: 
- Classes are balanced
- Both types of errors (FP and FN) have similar costs.
"""


from sklearn.metrics import accuracy_score

y_true = [1, 0, 1, 1, 0, 0, 1]
y_pred = [1, 0, 1, 0, 0, 0, 1]

accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy:.2f}")
