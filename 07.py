import numpy as np
a = np.array([[1,2,30],[10,15,4]])
print(a)
print(np.sqrt(a))
print(np.std(a))  
# ddof = 1 
# np.std(a, ddof=1) means population standard deviation (divides by N-1).
