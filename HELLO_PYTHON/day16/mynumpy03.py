# numpy 배열 비스무리한데 배열은 아닌거
import numpy as np

arr_n = np.ones((5, 4))

print(arr_n.shape)

arr_n2 = np.reshape(arr_n, (20)) #총 갯수가 같아야 됨

print(arr_n2)

