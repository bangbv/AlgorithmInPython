| Metric      | Definition                                             | Best For                                         | Weakness                                          |
|-------------|--------------------------------------------------------|--------------------------------------------------|---------------------------------------------------|
| Accuracy    | (TP + TN) / (TP + TN + FP + FN)                        | Balanced datasets                                | Misleading on imbalanced data                    |
| Precision   | TP / (TP + FP)                                         | Minimizing false positives (e.g., spam filters)     | Can ignore false negatives                        |
| Recall      | TP / (TP + FN)                                         | Minimizing false negatives (e.g., cancer detection) | Can ignore false positives                        |
| F1 Score    | Harmonic mean of precision and recall                  | When you need a balance between precision & recall             | Doesn't distinguish between FP and FN            |
| ROC AUC     | Area under the ROC curve                               | Overall ability to rank positives higher          | Not focused on threshold-specific performance     |
| PR AUC      | Area under the Precision-Recall curve                  | Imbalanced datasets, positive class focus         | Can be harder to interpret                        |
