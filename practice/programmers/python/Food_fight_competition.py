# my sol
def solution(food):
    ans = ""
    stack = ""
    for i in range(len(food)):
        if i == 0:
            ans += '0'
        else:
            stack += (str(i) * (food[i]//2))
    ans = stack + ans + stack[::-1]
    return ans
  
  
  
# other sol
def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer
