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
