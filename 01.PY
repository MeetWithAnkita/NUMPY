# 1. numpy install 
# 2. list to ndarray create 
import numpy as np

data1 = [1,2,3,4,5]
arr1 = np.array(data1)
print(data1, type(data1))
print(arr1, type(arr1))


# create ndarrays from lists
# note: every element must be the same data type (will be converted is possible)
data2 = [1,2.2,3,4,5]
arr2 = np.array(data2)  #upcasting work here 
                        # int + float → float
                        # int + float + complex → complex
                        # int + string → string (object/unicode)
print(data2, type(data2))
print(arr2, type(arr2), arr2.dtype)
