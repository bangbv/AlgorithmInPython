from sklearn.metrics import precision_score

"""
Precision=TP​/(TP+FP)
Ex: Of everything the model predicted as positive, how many were truly positive?”
Imagine your model predicts 10 emails as spam, but only 6 of them actually are.
Precision = 6 / (6 + 4) = 0.6
Scenario	        | Why Precision Matters
Email Spam Filter   | Don’t wrongly send important emails to spam.
Face Recognition	| Minimize false matches with wrong individuals.
Medical Tests	    | Minimize telling healthy people they’re sick.
"""

y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1]

precision = precision_score(y_true, y_pred)
print(f"Precision: {precision:.2f}")
