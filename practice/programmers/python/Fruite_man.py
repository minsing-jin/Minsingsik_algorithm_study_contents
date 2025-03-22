# my sol
def solution(k, m, score):
    score.sort(reverse = True)
    tmp = []
    ans = 0
    for i in range(len(score)):

        tmp.append(score[i])
        if len(tmp) == m:
            ans += min(tmp)*m
            tmp = []

    return ans

# other sol

def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m
