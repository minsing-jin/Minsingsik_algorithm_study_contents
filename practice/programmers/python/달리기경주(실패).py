def solution(players, callings):
    players_rank = [i for i in range(len(players))]

    for i in callings:
        players_rank[players_rank.index(players_rank[players.index(i)]-1)] += 1
        players_rank[players.index(i)] -= 1


    # 여기까지는 players의 인덱스 순서대로 rank를 매겼음. 이 순서대로 어떻게 append를 할것인가?

    rank_dic = dict(zip(players,players_rank))

    ans = sorted(rank_dic.items(), key=lambda x: x[1])

    return [ans[i][0] for i in range(len(ans))]

  
  #시간초과 이슈
  # 아래는 연습용코드
  
  
players = ["mumu", "soe", "poe", "kai", "mine"]
players_rank = [i for i in range(len(players))]
callings = ["kai", "kai", "mine", "mine"]
# print(players_idx)
# 인덱스 값 가지고 놀기
# players.index(i)는 고유 위치값
# players_idx는 rank
for i in callings:
    players_rank[players_rank.index(players_rank[players.index(i)]-1)] += 1
    players_rank[players.index(i)] -= 1
    
    print(players_rank)

    
# 여기까지는 players의 인덱스 순서대로 rank를 매겼음. 이 순서대로 어떻게 append를 할것인가?

rank_dic = dict(zip(players,players_rank))
print(rank_dic)
print(len(rank_dic))
# print(rank_dic[0])
ans = sorted(rank_dic.items(), key=lambda x: x[1])

real_ans = [ans[i][0] for i in range(len(ans))]
print(real_ans)        
