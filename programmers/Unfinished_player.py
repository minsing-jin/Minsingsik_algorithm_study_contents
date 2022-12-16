# my sol
def solution(participant, completion):

    participant.sort()
    completion.sort()

    for i in range(len(completion)):

        if completion[i] != participant[i]:
            return participant[i]
          
          
# other sol
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
  
  
  
  
# 해쉬를 통해서 dictionary로 접근하면 탐색 속도 향상
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
