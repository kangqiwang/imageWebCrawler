import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

df = pd.read_csv("test_data1_and_name.csv", usecols=['distance', 'colorSimilarity', 'result'])
df=df.sample(1000)
X = df.values

X = np.array([x.astype(float) for x in X if
              x[0] != '-1' and x[0] != 'None' and x[0] != 'ERROR' and x[1] != -1.0 and x[0] !=-1 and not np.isnan(x[1]) and not np.isnan(x[0])])


y = X[:, [2]]
X = np.delete(X, [2], axis=1)
colors=['red','blue']
y=y.flat
print(np.shape(X))
print(X[:,[0]])
print(y)
plt.scatter(X[:,0],X[:,1],c=y)

plt.legend()
plt.show()
