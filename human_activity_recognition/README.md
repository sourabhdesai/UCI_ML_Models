# RESULTS

## Random Forest

### Accuracy
92.534%

### Confusion Matrix

| WALKING | WALKING_UPSTAIRS | WALKING_DOWNSTAIRS | SITTING | STANDING | LAYING |
|---------|------------------|--------------------|---------|----------|--------|
| 479     | 13               | 4                  | 0       | 0        | 0      |
| 35      | 430              | 6                  | 0       | 0        | 0      |
| 19      | 43               | 358                | 0       | 0        | 0      |
| 0       | 0                | 0                  | 438     | 53       | 0      |
| 0       | 0                | 0                  | 47      | 485      | 0      |
| 0       | 0                | 0                  | 0       | 0        | 537    |

### Non-Default Hyperparameters
- n_estimators=75

