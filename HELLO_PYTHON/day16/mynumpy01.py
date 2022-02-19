# numpy 배열 비스무리한데 배열은 아닌거
import numpy as np

arr = [1,2,3]
print(arr)

arr_n = np.array(arr)
print(arr_n * 2)    # 사칙 연산이 유효함