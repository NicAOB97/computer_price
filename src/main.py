import pandas as pd
import numpy as np 
import seaborn as sns

from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from functions import ram_name, memory_type, screen_res_type, gpu, cpu


train = pd.read_csv('./precio-de-las-laptop/train.csv')
test = pd.read_csv('./precio-de-las-laptop/test.csv')

# preprocess training data
train = ram_name(train)
train = memory_type(train)
train = screen_res_type(train)
train = gpu(train)
train = cpu(train)

# set x and y variables
x = train[['Ram', 'Inches', 'Memory_Type', 'Mobile', 'Discrete','cpu_GHz', 'Touchscreen','HD']]
comp_dummies = pd.get_dummies(train['TypeName'])
x = pd.concat([x, comp_dummies], axis=1)

y = train['Price_euros']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

# scale data
scaler = StandardScaler()
scaler.fit(x)
x_scale = scaler.transform(x)
# create model (linear regression)
lm = LinearRegression()
lm.fit(x_train, y_train)
y_pred = lm.predict(x_test)
sns.regplot(y_test, y_pred)

# print results 
print('MAE:', mean_absolute_error(y_train, lm.predict(x_train)))
print('MSE:', mean_squared_error(y_train, lm.predict(x_train)))
print('RMSE:', np.sqrt(mean_squared_error(y_train, lm.predict(x_train))))

print('MAE test:', mean_absolute_error(y_test, lm.predict(x_test)))
print('MSE test:', mean_squared_error(y_test, lm.predict(x_test)))
print('RMSE test:', np.sqrt(mean_squared_error(y_test, lm.predict(x_test))))

# preprocess testing data
train = ram_name(train)
train = memory_type(train)
train = screen_res_type(train)
train = gpu(train)
train = cpu(train)

# set x_test and scale
x_test = test[['Ram', 'Inches', 'Memory_Type', 'Mobile', 'Discrete','cpu_GHz', 'Touchscreen','HD']]
comp_dummies = pd.get_dummies(test['TypeName'])
x_test = pd.concat([x_test, comp_dummies], axis=1)
x_test_scaled = scaler.transform(x_test)

# predict 
predictions_submit = lm.predict(x_test)

