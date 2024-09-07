def f2c(temp_f):
    return (temp_f - 32) * 5 / 9

def c2f(temp_c):
    return (temp_c * 9 / 5) + 32


def main():
    temp = input("화씨와 섭씨 중 어떤 단위로 바꾸실 건가요? (화씨/섭씨): ")

    if temp == "화씨":
        temp_f = float(input("화씨 온도를 입력하세요."))
        temp_c = f2c(temp_f)
        print(f"{temp_f}Ｆ -> {temp_c}℃")

    elif temp == "섭씨":
        temp_c = float(input("섭씨 온도를 입력하세요."))
        temp_f = c2f(temp_c)
        print(f"{temp_c}℃ -> {temp_f}Ｆ")

    else:
        print("'화씨' 와 '섭씨' 중 입력해 주세요.")


if __name__=="__main__":
    main()