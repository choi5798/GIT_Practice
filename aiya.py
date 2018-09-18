def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

n = int(input("n 팩토리얼의 값을 구해줍니다. n을 입력하세요 : "))
print("값은 : " + str(fact(n)))
print('Hello World!')