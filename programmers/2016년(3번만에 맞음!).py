# 해결!

# my sol

def solution(a, b):
    
    n = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    D = ['THU','FRI','SAT','SUN', 'MON','TUE','WED']
    if a == 1:
        return D[b%7]
    else:
        
        return  D[((sum(n[:a])+b)%7)] 


# 틀린풀이 -> line 11에 index out of range와 더불어 n에서 a의 당월은 31일같은 일수를 세면 안돼는데 세서 실패했었음!

def solution(a, b):
    
    n = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    D = ['MON','TUE','WED', 'THU','FRI','SAT','SUN']
    if a == 1:
        return D[b%7 + 3]
    else:
        
        return  D[((sum(n[:a+1])+b-1)%7)]  -> 여기서부터 index out of range가 걸림
    
      
      # 어디서 예외가 발생한것이지? 이런거 해결하려면 일일이 다 대입해보고 맞나 틀리나해야함?
      
      
 # 옳은 풀이

def solution(a, b):
    answer = 0
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    
    for i in range(a-1):
      answer += months[i]
    
    answer += b-1
    answer = answer%7
    
    return days[answer]
