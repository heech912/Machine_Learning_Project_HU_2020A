import h5py
import datetime as dt

### .mat file의 Data를 Import 해서 List로 저장

## SCIPY DOES NOT WORK! : NotImplementedError: Please use HDF reader for matlab v7.3 files
# from scipy import io
#
# mat_file = io.loadmat('velocity_data/velocity_150.mat')
# print(mat_file)

## h5py로 1개 matfile 데이터 읽어들이기

filepath = 'matlab_data/velocity_150.mat'
f = h5py.File(filepath, 'r')
data = ''
for k, v in f.items():
    data = v

print(data[20][1])
print(len(data[3999]))

## noise 데이터파일 포맷팅
print (dt.datetime.now().strftime("%Y-%m%d-%H%M%S-%f"))
