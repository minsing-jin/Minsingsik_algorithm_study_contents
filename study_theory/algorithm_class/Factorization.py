# n 보다 작은 모든 소수의 리스트를 반환
def eratosthenes(n):
    sieve = [True] * n
    for i in range(2, n):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False     
    print([ i for i in range(2,n) if sieve[i] == True])           
    return [ i for i in range(2,n) if sieve[i] == True]

def primeFactor(n):
    # n과 같거나 작은 모든 소수를 원소로 가지는 리스트 생성
    l = eratosthenes(n+1)
    
    # l에 담긴 각 소수가 n의 소인수인지 확인해봅니다.
    i = 0
    result = []
    while i < len(l): 
        # To-do - pass는 지우고 코드를 작성해주세요. 
        # 1. 만약 현재 소수가 n의 소인수라면, result 리스트에 담고 n을 현재 소수로 나눕니다.
        # 2. 현재 소수가 n의 소인수가 아니라면 다음 소수로 넘어갑니다. 
        while True:
            if n%l[i] == 0:
                result.append(l[i]) 
                n = n//l[i]  
            else:
                break
        i+=1
    return result
    

# 결과 출력을 위한 코드입니다. 자유롭게 값을 바꿔보며 확인해보세요.
print(primeFactor(10))
