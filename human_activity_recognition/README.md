# Dataset
- This is a dataset of human activity as detected by various sensors on a Smartphone.
- [Dataset overview](https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones)
- [Direct Download Link](https://archive.ics.uci.edu/ml/machine-learning-databases/00240/)
 - To run the scripts, put the files from the downloaded unpacked zip file into a directory here called `data/`

# Results

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

