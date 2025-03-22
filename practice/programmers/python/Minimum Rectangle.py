# my sol
def solution(sizes):
    long_di = []
    short_di = []
    for i in sizes:
        long_di.append(max(i[0], i[1]))
        short_di.append(min(i[0],i[1]))


    return max(long_di)*max(short_di)
  
# other sol
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

  
  
  
  
  
  
  
  
  
# feed back
"""
너무 어렵게 생각해서 그렇다. 쉬운 아이디어로 쉽게 쉽게 접근하자!
잘 안되면 모양으로 생각하기/ 그리면서 생각하기

1. 도움받은 question
모든 명함들의 긴 모서리를 가로로 돌려서 겹쳐봅시다.
그 상태에서 지갑에 한번에 넣을 수 있으려면 세로길이는 어떻게 해야할지 상상해봅시다!
"""
