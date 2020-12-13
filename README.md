# Machine_Learning_Project_HU_2020A

Electric Motor Torque Constant Estimation & Cargo Mass Regression in EV trolley  

Machine Learning 해석 CLI 소프트웨어  

B717120 이한결  
B735520 최희찬  

## Configuration  
Python 3.8.2 이상  
PIP 20.3.1 이상  
Dependencies   
* h5py : matfile load (pip install 시 wheel 이슈 해결을 위해 versioned-hdf5 설치 권장 )
```{.bash}
py -m pip install versioned-hdf5
py -m pip install h5py
```
* numpy : 행렬연산  
```{.bash}
py -m pip install numpy
```
* matplotlib : visualization
```{.bash}
py -m pip install matplotlib
```
* datetime(built-in) : data 추출 시간 
* (scipy) : mat 파일 load, 단 matlab v7.3 파일에는 불가
