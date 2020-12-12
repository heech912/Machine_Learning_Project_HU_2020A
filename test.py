### .mat file의 Data를 Import 해서 List로 저장

## SCIPY DOES NOT WORK! : NotImplementedError: Please use HDF reader for matlab v7.3 files
# from scipy import io
#
# mat_file = io.loadmat('velocity_data/velocity_150.mat')
# print(mat_file)


import h5py
import numpy as np
filepath = 'velocity_data/velocity_150.mat'
arrays = {}
f = h5py.File(filepath, 'r')
for k, v in f.items():
    arrays[k] = np.array(v)
print(arrays)
