from util import *
from mode import create_train_data, train_regression, estimation

title()
mode = ""
ENDCODE = "4"

while mode != ENDCODE :
    mode = menu()
    if mode == "1":
        create_train_data()
    elif mode == "2":
        train_regression()
    elif mode == "3":
        estimation()



print("\n프로그램이 종료되었습니다.")
