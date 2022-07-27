# my sol
def solution(N, stages):
    tmp = [] # 1~n등 실패율
    player = [] # 스테이지 도달한 플레이어수

    # 스테이지 실패율
    for i in range(1,N+1):
    #     print(i)
        for n in stages:
            if i <= n:
                player.append(n)

        try:
            tmp.append(stages.count(i)/len(player))

            player = []

        except:
            tmp.append(0)
            player = []


    dictionary = dict(zip(range(1,len(tmp)+1), tmp)) # {스테이지:실패율}


    # 아예 딕셔너리에서 value값들을 랭킹해버리기

    dictionary = sorted(dictionary.items(), reverse = True, key = lambda x: x[1])


    ans = []
    for i in range(len(dictionary)):
        ans.append(dictionary[i][0])
    return ans

  
  # other sol
  def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
