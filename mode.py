import h5py
import datetime as dtm
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

from util import prnt

def estimation():
    trlf =  open("train_results/trainResults_List.txt", "r")
    a = trlf.read().split('\n')
    a.pop(len(a)-1)
    a.sort(reverse=True)
    prnt("다음 중 Esitimation을 진행할 train result set를 선택하세요.")
    for idx, val in enumerate(a):
        prnt(str(idx)+ " : " + val)
    try :
        dataSet_num = int(input("\n   train result set 선택 >>> "))
    except :
        prnt("올바른 숫자를 입력하세요.")
    tf = open("train_results/"+a[dataSet_num] + ".txt", "r")
    b = tf.read().split('\n')
    b.pop(len(b)-1)
    b.sort(reverse=True)
    prnt("다음 중 Esitimation을 진행할 학습 파라미터를 선택하세요.")
    for idx, val in enumerate(b):
        prnt(str(idx)+ " : " + val)
    try :
        param_num = int(input("\n   학습 파라미터 선택 >>> "))
    except :
        prnt("올바른 숫자를 입력하세요.")
    param = b[param_num].split(' / ')
    opt_slope = float(param[0].split(' ')[1])
    opt_yint = float(param[1].split(' ')[1])
    std = float(param[3].split(' ')[1])
    e_p = float(param[4].split(' ')[1])
    testf =  open("test_data/testData_List.txt", "r")
    c = testf.read().split('\n')
    c.pop(len(c)-1)
    prnt("다음 중 Esitimation의 대상이 되는 가상 test data를 선택하세요.")
    for idx, val in enumerate(c):
        prnt(str(idx)+ " : " + val)
    try :
        test_num = int(input("\n   test data 선택 >>> "))
    except :
        prnt("올바른 숫자를 입력하세요.")
    test_data_name = c[test_num]
    tdf = open("test_data/"+ test_data_name +".txt", "r")
    d = tdf.read().split('\n')
    raw_data = d[1:]
    raw_data.pop(len(raw_data)-1)
    max_val = std * (1+e_p/100)
    min_val = std * (1-e_p/100)
    for data in raw_data:
        temp_val = data.split("/")
        if min_val<float(temp_val[1])<max_val:
            time =float(temp_val[0])
            break
    estimated_val =(time - opt_yint) / opt_slope
    prnt("추정 질량값 : " + str(estimated_val))
    prnt("오차 : " + str( abs (100 * (float(d[0])-estimated_val)/float(d[0])) ) + " %" )






def train_regression():
    tlf =  open("train_data/trainData_List.txt", "r")
    a = tlf.read().split('\n')
    a.pop(len(a)-1)
    a.sort(reverse=True)
    prnt("다음 중 Regression을 진행할 실험 Data를 선택하세요.")
    for idx, val in enumerate(a):
        prnt(str(idx)+ " : " + val)
    try :
        dataSet_num = int(input("\n   Train Data 선택 >>> "))
    except :
        prnt("올바른 숫자를 입력하세요.")
    prnt("실험데이터를 읽어들입니다. 시간이 조금 소요됩니다..")
    tf = open("train_data/"+a[dataSet_num] + ".txt", "r")
    dt = []
    dataArr = tf.read().split("\n\n")
    dataArr.pop(len(dataArr)-1)
    for data in dataArr:
        data = data.split("\n")
        dt.append(data)
    prnt("실험데이터를 모두 읽어들였습니다.")
    trainResults_Name = "trainResults-"+dtm.datetime.now().strftime("%Y-%m%d-%H%M%S-%f")
    trf = open("train_results/"+trainResults_Name+".txt", "a")
    trlf = open("train_results/trainResults_List.txt", "a")
    trlf.write(trainResults_Name+"\n")
    istesting = True
    while istesting:
        lam = 0
        prnt("Regression을 위한 parameter들을 입력하세요.")
        standard = float(input("\n   기준값 >>> "))
        err_percent = float(input("\n   기준값과의 오차(%) >>> "))
        regression_type = int(input("\n   1. Pure Linear Regression  2. L1 Normalization  3. L2 Normalization >>> "))
        if (regression_type != 1):
            lam = float(input("\n   lambda for Normalization  >>> "))
        max_val = standard * (1+err_percent/100)
        min_val = standard * (1-err_percent/100)
        threshold_x = []
        threshold_y = []
        for data in dt:
            x = data[0]
            y = data[1:]
            idx = 0
            isFound = False
            while idx < len(y) and (not isFound):
                temp_val = y[idx].split("/")
                if min_val<float(temp_val[1])<max_val:
                    isFound = True
                    threshold_x.append(int(x))
                    threshold_y.append( float(temp_val[0]))
                idx += 1
        y = np.array([threshold_y]).T
        pi = np.array([ np.ones(len(threshold_x)).T,np.array(threshold_x).T]).T
        if regression_type == 1:
            optimal_parameters = inv(pi.T @ pi)@pi.T@y
        elif regression_type == 2:
            optimal_parameters = inv(pi.T @ pi)@(pi.T@y - (lam/2)* np.array([[1,1]]).T)
        elif regression_type == 3:
            optimal_parameters = inv(pi.T @ pi + lam* np.identity(2))@pi.T@y
        else :
            prnt("올바른 regression_type을 입력해주세요.")
        optimal_values = optimal_parameters[1] * threshold_x + optimal_parameters[0]
        mean = np.mean(y)
        sstot = 0
        ssres = 0
        for y_idx, y_val in enumerate(y):
            sstot += (y_val - mean)**2
            ssres += (y_val - optimal_values[y_idx])**2
        RSS = 1- (ssres/sstot)
        trf.write("slope " + str(optimal_parameters[1][0]))
        trf.write(" / y_intercept " + str(optimal_parameters[0][0]))
        trf.write(" / RSS " + str(RSS) )
        trf.write(" / standard "+ str(standard))
        trf.write(" / err_percent " + str(err_percent))
        trf.write(" / regression_type " + str(regression_type))
        trf.write(" / lambda " + str(lam) + '\n')
        plt.plot(threshold_x, threshold_y, 'go', threshold_x, optimal_values, 'r')
        plt.title("Train : " + dtm.datetime.now().strftime("%Y.%m.%d/%H:%M:%S\n t = " +str(optimal_parameters[1]) +" m + "+str(optimal_parameters[0]) + ", RSS : " + str(RSS) ))
        plt.ylabel("Reach Time")
        plt.xlabel("Expermiental Mass")
        plt.show()
        finish = input("\n   종료하시려면 N, 다시하시려면 아무키나 누르세요 >>>")
        if finish == "N":
            istesting = False






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
    trainData_Name = "trainData-"+dtm.datetime.now().strftime("%Y-%m%d-%H%M%S-%f")
    tf = open("train_data/"+trainData_Name+".txt", "w")
    tlf = open("train_data/trainData_List.txt", "a")
    tlf.write(trainData_Name+"\n")
    for param in range(ans_start, ans_end + ans_interval, ans_interval):
        filepath = 'matlab_data/' + data_name +"_"+ str(param) + ".mat"
        f = h5py.File(filepath, 'r')
        dataArr = ""
        tf.write(str(param) + "\n")
        for label, raw_data in f.items():
            dataArr = raw_data
        for dataSet in raw_data:
            tf.write(str(dataSet[0]) + "/" + str(dataSet[1] + np.random.normal(cond_mean, cond_stdev)) + "\n")
        tf.write("\n")
    prnt("가상 실험 데이터 생성이 완료되었습니다 : " + trainData_Name)
