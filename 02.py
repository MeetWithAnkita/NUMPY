# list(range) to ndarray create (2D)
# list(range) to object : where two range are not same length
import numpy as np
data1 = [range(1,5), range(5,10)] 
# If inner sequences are unequal → NumPy falls back to dtype=object (basically an array of arbitrary Python objects).
data2 = [range(1,5), range(5,9)] 
# Since both have the same length (4 numbers), NumPy can make a 2D array (matrix).
arr1 = np.array(data1)
arr2 = np.array(data2)

print(data1, type(data1))
print(arr1, type(arr1), arr1.dtype)
print("___________")
print(data2, type(data2))
print(arr2, type(arr2), arr2.dtype)