# my solution 1
def solution(n):
    n_lst = []
    a_lst = []
    for i in range(2, n+1):
#         1~n까지 숫자 하나하나씩 소수판별 시작
        for x in range(1, i+1):
            if i % x == 0:
                n_lst.append(i)
        
        if len(n_lst) == 2:
            a_lst.append(n_lst[1])
            n_lst = []
        else:
            n_lst = []
    return len(a_lst)
    
# 시간 초과 issue 내일 마저 할것! -> 내일 했는데 1시간 이상 고민하면 퀘스쳔

# my trial
# n_lst가 2개 이상이면 break를 하고 다음 n으로 넘어가 소수판별을 하려고 했지만 이유도 모른채 실패
# i의 약수가 2개 이상 초과되면 break를 하고 그게 아니라면 1과 자기자신을 약수로 가지는것이므로 arg_num에
# += 1씩 더하려고 했지만 값이 이상하게 나옴
