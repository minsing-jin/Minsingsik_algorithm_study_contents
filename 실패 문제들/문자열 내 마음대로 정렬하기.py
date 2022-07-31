# 피드백
# 문자열 슬라이스하고, 문자열에 대해서 사고하는것이 굉장히 취약함! 문자열 공부 조금더 할것!
# 왜 못푼 문제는 답지를 보고 다음에 풀때 다시 또 막히는지? 이 문제를 외어야할지? 원리 이해만 하고 다시 할지?
# lambda 쓰는법 아직 취약
# list comprehension & if문 병합되어있는거 취약
# project로 실력을 올려야 하는지?

# 답지 sol
def solution (strings, n):
  new = []
  for i in strings:
    new.append(i[n]+i)
    new.sort()
    answer = []
    for i in new:
      answer.append(i[1:])
    return answer
  
#other good sol
def solution(strings,n):
  return sorted(strings, key = lambda x: (x[n], x)) 
