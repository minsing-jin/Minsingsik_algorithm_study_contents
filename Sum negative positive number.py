# my sol
def solution(absolutes, signs):
    ans = 0
    for i in range(len(signs)):
        if signs[i] == True:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]

    return ans


# other sol
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

# [ 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in data] 
