my sol
def solution(t, p):
    tmp = [t[i:i+len(p)] for i in range(len(t)-len(p)+1) ]
    ans = 0
    for n in tmp:
        if n <= p:
            ans += 1

    return ans


# other sol

def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer
