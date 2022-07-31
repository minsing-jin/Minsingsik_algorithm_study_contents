"""문제
1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 

단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.
"""

# my long solution
def solution(num):
    cnt = 0
    answer = 0
    while True:
        if cnt >500:
            return -1
        else:
            if num%2 == 0:
                num = num/2
                cnt += 1
            elif num == 1:
                answer = cnt
                break
            elif num%2 != 0:
                num = 3*num + 1
                cnt += 1



    return answer

# legend solution
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
