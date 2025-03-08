import pandas as pd
import numpy as np
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)

#1.⁠ ⁠From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
filtered = df.loc[::20, ["Manufacturer", "Model", "Type"]]
print(filtered)

#2.⁠ ⁠Replace missing values in Min.Price and Max.Price columns with their respective mean.
for i in ["Min.Price", "Max.Price"]:
    if i in df.columns:
        df[i] = df[i].fillna(df[i].mean())

#3.⁠ ⁠How to get the rows of a dataframe with row sum > 100?
df_random = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
row = df_random[df_random.sum(axis=1) > 100]
print("\nSum > 100:\n", row)


import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

#1.⁠ ⁠Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.
A = np.array([1, 2, 3])
B = np.array([3, 4, 5])
vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

#2.⁠ ⁠Find common elements between A and B. [Hint : Intersection of two sets]
common_elements = np.intersect1d(A, B)

#3.⁠ ⁠Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]
range_mask = (A >= 5) & (A <= 10)
num = A[range_mask]

#4.⁠ ⁠Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
filter = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
rows = iris_2d[filter]

