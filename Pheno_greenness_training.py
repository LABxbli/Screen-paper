import pandas as pd
from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split
import joblib

dat = pd.read_excel( 'RGB_score.xlsx', header = 0 )

dat = dat[ [ 'Red', 'Green', 'Blue', 'Score' ] ]
x, y = np.split( dat, (3,), axis=1 )	# 
x_train, x_test, y_train, y_test = train_test_split( x, y, random_state=1, train_size=0.7 )
clf = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr' )

clf.fit( x_train, y_train.values.ravel() )

print( clf.score( x_train, y_train ) )
print( clf.score( x_test, y_test ) )

# clf.predict( [[ 0, 0, 0] ] ).item()
joblib.dump(clf, 'model.svm.linear.pkl' )
