import numpy as np 

arr = np.array([[1,2,3,4],
                [5,6,7,8]])
print(arr)
arr2 = np.array([range(1,5),range(5,11)],dtype = object)
# dtype have to use for ragged or not rectangular array
print(arr2)

print("type()>>>>>>>>>>")
print(type(arr),type(arr2))
print("id()>>>>>>>>>>")
print(id(arr),id(arr2))
print(".dtype>>>>>>>>>>")
print(arr.dtype,arr2.dtype)
print(".shape>>>>>>>>>>")
print(arr.shape,arr2.shape)
print(type(arr.shape),type(arr2.shape))
print(".ndim>>>>>>>>>>")
print(arr.ndim,arr2.ndim)
# arr: two dimensions.
# arr2: only one dimension, because it’s just a flat array of 2 objects.
print(".size>>>>>>>>>>")
print(arr.size,arr2.size)
# arr: 8 numeric elements.
# arr2: only 2 objects (the two ranges).
print("len()>>>>>>>>>>")
print(len(arr),len(arr2))
# For both arrays, len() returns the length of the first axis
# arr → 2 rows.
# arr2 → 2 objects.