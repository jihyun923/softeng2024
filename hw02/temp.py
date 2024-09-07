def f2c(temp_f):
    return (temp_f - 32) * 5 / 9

def c2f(temp_c):
    return (temp_c * 9 / 5) + 32


def main():
    temp = input("(1) 화씨-> 섭씨 or (2) 섭씨 -> 화씨? (1/2): ")

    if temp == "1":
        temp_f = float(input("화씨 온도를 입력하세요."))
        temp_c = f2c(temp_f)
        print(f"{temp_f}Ｆ -> {temp_c:.1f}℃")

    elif temp == "2":
        temp_c = float(input("섭씨 온도를 입력하세요."))
        temp_f = c2f(temp_c)
        print(f"{temp_c}℃ -> {temp_f:.1f}Ｆ")

    else:
        print("'화씨' 와 '섭씨' 중 입력해 주세요.")


if __name__=="__main__":
    main()