
import numpy as np

a = np.array([[1, 4, 5], # numpy array
[-5, 8, 9],
[6, 8, 10], 
[0, 2, 38]])

print("type:", type(a)) 
print("a =","\n",a, "\n")
print("a[1]=", a[1])    # 2.satır
print("a[1][2]=", a[1][2]) #2.satırın 3.eleman
print("a[0][-1] =", a[0][-1]) # İlk satırın sonuncu elemanı