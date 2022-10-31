# my sol
def solution(a, b, n):
    real_coke = 0
    while True:
        if n < a:
            break
        if n%a == 0:
            real_coke += b*(n//a)
            n =  b*(n//a)
        else:
            real_coke += b*(n//a)
            n =  (n%a) + (n//a)*b


    return real_coke
 



# other sol1

solution = lambda a, b, n: max(n - b, 0) // (a - b) * b




# other sol2
def solution(a, b, n):
    answer = 0

    num = n
    while num >= a:
        cnt = num // a
        num -= (cnt * a)
        num += (cnt * b)
        answer += (cnt * b)


    return answe
  
# other sol 3
def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
    return answer
