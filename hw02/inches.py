def cm2inch(cm):
    return cm / 2.54

def inch2cm(inch):
    return inch * 2.54

def main():
    how = input("(1) 인치 -> 센티미터 or (2) 센티미터 -> 인치 : (1/2): ")

    if how == "1":
        inch = float(input("인치 단위로 값 입력 : "))
        cm = inch2cm(inch)
        print(f"{inch}inch -> {cm:.1f}cm")
    elif how == "2":
        cm = float(input("센티미터 단위로 값 입력: "))
        inch = cm2inch(cm)
        print(f"{cm}cm -> {inch:.1f}inch")
    else:
        print("1 또는 2를 입력해 주세요.")

if __name__ =="__main__":
    main()