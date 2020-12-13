import h5py
import datetime as dt
import numpy as np
from numpy.linalg import inv

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
print(np.random.normal(0,1))
## noise 데이터파일 포맷팅
print (dt.datetime.now().strftime("%Y-%m%d-%H%M%S-%f"))

## python file i/o
tlf = open("train_data/trainData_List.txt", "r")
a = tlf.read().split('\n')
a.pop(len(a)-1)
a.sort(reverse=True)
for idx, val in enumerate(a):
    print(str(idx)+ " : " + val)

tf = open("train_data/"+"trainData-2020-1213-120627-916633"+ ".txt", "r")
dt = []
dataArr = tf.read().split("\n\n")
dataArr.pop(len(dataArr)-1)
for data in dataArr:
    data = data.split("\n")
    dt.append(data)

## Numpy Mat Ops
A = np.array([[1,1],[2,3]])
B = np.array([[1,0],[0,1]])
print(A.T)

x= [1,2.2,3]
y = np.array([[3,6,4]]).T
pi = np.array([ np.ones(len(x)).T,np.array(x).T]).T
print(y.shape)
print(pi)
print(pi.shape)
print(inv(pi.T @ pi)@pi.T@y)

## 수동 데이터 추출
def test_create_train_data(num, mean, stdev):
    tlf = open("test_data/testData_List.txt", "a")
    tf = open( "test_data/velocity_"+str(num)+"("+str(mean)+"_"+str(stdev)+")" +".txt", "a")
    tlf.write('velocity_'+ str(num) +  "(" + str(mean)+"_"+str(stdev) + ")"+ "\n")
    filepath = 'test_data/velocity_'+ str(num) + ".mat"
    f = h5py.File(filepath, 'r')
    dataArr = ""
    tf.write(str(num) + "\n")
    for label, raw_data in f.items():
        dataArr = raw_data
    for dataSet in raw_data:
        tf.write(str(dataSet[0]) + "/" + str(dataSet[1] + np.random.normal(mean, stdev)) + "\n")

##DANGER : DO NOT UNCOMMENT THESE CODES WITHOUT CAUTION
# test_create_train_data(167, 0.0, 0.5)
# test_create_train_data(223, 0.0, 0.5)
# test_create_train_data(257, 0.0, 0.5)
# test_create_train_data(333, 0.0, 0.5)
#
# test_create_train_data(167, 0.0, 0.3)
# test_create_train_data(223, 0.0, 0.3)
# test_create_train_data(257, 0.0, 0.3)
# test_create_train_data(333, 0.0, 0.3)
