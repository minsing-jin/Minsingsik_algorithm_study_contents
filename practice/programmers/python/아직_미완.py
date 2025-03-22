def solution(number):
    answer = 0
    number.sort()
    for i in number:
        tmp = number
        tmp.remove(i)
        
        # 0이 존재할때 변수 고려
        
        if 0 in tmp:
            if -i in tmp:
                answer += 1
        for n in range(len(tmp)-1):
            if i == -sum(tmp[n:n+2]):
                answer += 1
        
        
    return answer

# 모든 경우의 수를 다 흝는 방법/인접한 녀석과 둘이 더해서 같은걸 찾는건 놓치는 경우의 수가 있음/ 0이 sort한 상황에서는 다른 경우의 수를 만들어내는 변수임!
