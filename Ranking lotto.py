#my sol
def solution(lottos, win_nums):
    win_cnt = 0
    
    for i in lottos:
        for x in win_nums:
            if i == x:
                win_cnt += 1
                
    max = lottos.count(0) + win_cnt
    min = win_cnt
    
    ans = []
    
    if max == 6:
        ans.append(1)
    elif max == 5:
        ans.append(2)
    elif max == 4:
        ans.append(3)
    elif max == 3:
        ans.append(4)
    elif max == 2:
        ans.append(5)
    else:
        ans.append(6)
        
    
    if min == 6:
        ans.append(1)
    elif min == 5:
        ans.append(2)
    elif min == 4:
        ans.append(3)
    elif min == 3:
        ans.append(4)
    elif min == 2:
        ans.append(5)
    else:
        ans.append(6)
        
    
    return ans
  
# other sol
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

  
  # rank를 리스트로 보는생각
