import pandas as pd
from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split
import joblib

# dat = pd.read_excel( 'Random_selected_1500.xlsx', header = 0 )
dat = pd.read_excel( 'RGB_score.xlsx', header = 0 )
# R	G	B	Score
# 4	29	6	1000
# 5	27	2	1000
# 2	35	1	990
dat = dat[ [ 'Red', 'Green', 'Blue', 'Score' ] ]
x, y = np.split( dat, (3,), axis=1 )	# 
x_train, x_test, y_train, y_test = train_test_split( x, y, random_state=1, train_size=0.7 )
clf = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr' )
# clf = svm.SVC( C=0.8, kernel='rbf', gamma=10, decision_function_shape='ovr' )
# clf = svm.SVC( kernel='linear' )
clf.fit( x_train, y_train.values.ravel() )



print( clf.score( x_train, y_train ) )
print( clf.score( x_test, y_test ) )

# clf.predict( [[ 0, 0, 0] ] ).item()
joblib.dump(clf, 'model.svm.linear.pkl' )
