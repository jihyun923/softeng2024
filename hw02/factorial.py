def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    n = int(input("수를 입력해 주세요. "))
    fact = factorial(n)
    print(f"최종값은 {fact}입니다.")

if __name__ =="__main__":
    main()