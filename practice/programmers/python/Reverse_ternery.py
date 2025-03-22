# my sol
def solution(n):
    tmp = []
    if n == 1:
        return n

    while True:
        tmp.append(n%3)

        if (n // 3) < 3:
            tmp.append(n//3)
            break

        n = n//3


    answer = []
    factor = len(tmp)-1

    for i in tmp:   
        answer.append(i*(3**factor))
        factor = factor - 1

    return sum(answer)


# other sol

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
