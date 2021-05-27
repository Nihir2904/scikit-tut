
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])

diabetes = datasets.load_diabetes()
print(diabetes.keys())


diabetes_x = diabetes.data

diabetes_x_train = diabetes_x[:-30]
diabetes_x_test = diabetes_x[-30:]

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()
model.fit(diabetes_x_train, diabetes_y_train)

diabetes_y_predicted = model.predict(diabetes_x_test)

print("mean_squared_error is:", mean_squared_error(diabetes_y_test, diabetes_y_predicted))

print("weights:", model.coef_)
print("intercepts:", model.intercept_)

"""plt.scatter(diabetes_x_test, diabetes_y_test)
plt.plot(diabetes_x_test, diabetes_y_predicted)
plt.show()"""
#  mean_squared_error when only one feature was considered: 3035.0601152912695
