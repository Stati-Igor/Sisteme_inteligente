import numpy as np
from numpy.core.fromnumeric import take
from numpy.core.numeric import ones
from numpy.core.records import array
from numpy.lib.stride_tricks import sliding_window_view
a=np.array([1,2,3,4,5])
print(a)  
print(a.dtype) #tipul de date
print(a.shape)  #lungimea 
print(a[4]) #arata elementul cu indexul  4

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[0][2]) #arata elementul cu indexul 0 2
print(np.sum(b)) #arata suma tuturor elementelor
print(np.average(b)) #arata media aritmetica a tuturor elementelor
print(np.sum(b, axis=(1))) #arata suma pe orizontala (axa 1)
print(b)

zero_array = np.zeros((3,3)) #tabel din zerouri 3x3
print(zero_array)

ones_array = np.ones((3,3)) #tabel din cifra 1 3x3
print(ones_array)

constant_array =np.full((2,2),8) #tabel din cifra 8 2x2
print(constant_array)

identity_matric = np.eye(4) # matrice cu diagonala 1
print(identity_matric)