import h5py
import datetime as dt
import numpy as np

from util import prnt

def create_train_data():
    prnt("matlab data로부터 noise를 첨가한 가상 실험 데이터를 생성합니다.")
    inputs_fine = False
    while not inputs_fine:
        data_name = input("\n   데이터 이름 >>> ")
        try :
            ans_start = int(input("\n   실험변인 시작값(int) >>> "))
            ans_end = int(input("\n   실험변인 종료값(int) >>> "))
            ans_interval = int(input("\n   실험변인 간격(int) >>> "))
            cond_mean = float(input("\n   noise mean(float) >>> "))
            cond_stdev = float(input("\n   noise stdev(float) >>> "))
        except :
            prnt("올바른 숫자(int/float)를 입력해주세요.")
        else :
            inputs_fine = True
    prnt("가상 실험 데이터를 생성합니다. 시간이 소요될 수 있습니다..")
    trainData_Name = "trainData-"+dt.datetime.now().strftime("%Y-%m%d-%H%M%S-%f")
    tf = open("train_data/"+trainData_Name+".txt", "w")
    tlf = open("train_data/trainData_List.txt", "a")
    tlf.write("/n"+trainData_Name)
    for param in range(ans_start, ans_end - ans_interval, ans_interval):
        filepath = 'matlab_data/' + data_name +"_"+ str(param) + ".mat"
        f = h5py.File(filepath, 'r')
        dataArr = ""
        tf.write("\n" + str(param) + "\n")
        for label, raw_data in f.items():
            dataArr = raw_data
        for dataSet in raw_data:
            for data in dataSet:
                tf.write(str(data) + " ")
            tf.write("/ ")
    prnt("가상 실험 데이터 생성이 완료되었습니다 : " + trainData_Name)
