# list ==> array => list

import numpy as np
list1 = [range(1,5), range(10,14)]
arr1 = np.array(list1) 
# list converted to array 
print(arr1, type(arr1))
# array convert to list 
list2 = arr1.tolist()
print(list2, type(list2))
