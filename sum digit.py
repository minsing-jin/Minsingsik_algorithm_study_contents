# 자릿수 더하기
def solution(n):
    x = str(n)
    a = 0
    for i in range(len(x)):
        a += int(x[i])

    return a

# 재귀 풀이

def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)    # 여기서 12 line sum_digit함수를 다시 호출하면서 재귀 구조 만듬

# 한줄 풀이

def sum_digit(number):
    return sum([int(i) for i in str(number)])
