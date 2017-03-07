import numpy as np
import sklearn
from numpy import genfromtxt
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import confusion_matrix

labels = ['WALKING', 'WALKING_UPSTAIRS', 'WALKING_DOWNSTAIRS', 'SITTING', 'STANDING', 'LAYING']

x_train = genfromtxt('../data/train/X_train.txt')
y_train = genfromtxt('../data/train/Y_train.txt')

x_test = genfromtxt('../data/test/X_test.txt')
y_test = genfromtxt('../data/test/Y_test.txt')

param_grid = {'n_estimators': [75]}

rfc = RandomForestClassifier()

classifier = GridSearchCV(rfc, param_grid)

classifier.fit(x_train, y_train)


y_test_results = np.array([classifier.predict(x) for x in x_test])

accuracy = accuracy_score(y_test, y_test_results)

def convert_y_to_labels(y_values):
    return [labels[int(y-1)] for y in y_values]

print('accuracy', accuracy)
print ('best score', classifier.best_score_)
print ('best params', classifier.best_params_)
print ('confusion matrix', confusion_matrix(convert_y_to_labels(y_test), convert_y_to_labels(y_test_results), labels=labels))







