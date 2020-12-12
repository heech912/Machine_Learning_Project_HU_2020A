def prnt(text):
    print("\n   " + text)

def title():
    prnt("")
    prnt("  #################################")
    prnt("  Machine_Learning_Project_HU_2020A")
    prnt("   B717120 이한결  B735520 최희찬")
    prnt("  #################################")
    prnt("")

def menu():
    prnt("원하시는 메뉴를 선택하세요.")
    return input("\n   1. Train Data 생성하기  2. Train Data로 학습하기  3. 학습 결과로 질량 추정하기   4. 종료  >>> ")
