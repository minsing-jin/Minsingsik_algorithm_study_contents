# my sol
def solution(s):
    adjuster = 1
    distance = 1
    ans = []
    for i in range(len(s)):

        if i == 0:
            ans.append(-1)
        else:
            while True:
                if i-adjuster < 0:
                    ans.append(-1)
                    distance = 1
                    adjuster = 1
                    break
                else:

                    if s[i] == s[i-adjuster]:
                        ans.append(distance)
                        distance = 1
                        adjuster = 1
                        break
                    else:
                        distance += 1
                        adjuster += 1


    return ans
  
  
  
  
# other sol

def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer
