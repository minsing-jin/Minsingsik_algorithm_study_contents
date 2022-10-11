# 에라토스테네스의 체 방식인데 방식을 알려줘도 구현을 못함 ㅠㅠ


def solution(n):
    # n개의 True 값이 들어있는 목록을 준비 
    # (True는 소수, False는 합성수를 의미)
    sieve = [True] * n
    if n == 2:
        return 1
    # To-do - pass는 지우고 코드를 작성해주세요.
    # 2부터 n까지 하나씩 순차적으로 소수 여부를 판단
    for i in range(2, n):
        # 1. i가 소수인 경우 i의 배수를 False로 변경    
        # j 범위가 i+i에서 시작해서
        # n에서 종료하고
        # j의 값은 i씩 증가하라
        for j in range(i+i, n, i):
            sieve[j] = False

        # 2. i는 소수이므로 True값을 유지
        
        
        
    # 값이 True인 숫자를 추려낸다
#    result = []
#    for i in range(2, n):
#        if sieve[i] == True :
#            result.append(i)
    return len([i for i in range(2,n) if sieve[i] == True])
