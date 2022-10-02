# 졌다....

# 틀린풀이
def solution(a, b):
    
    n = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    D = ['MON','TUE','WED', 'THU','FRI','SAT','SUN']
    if a == 1:
        return D[b%7 + 3]
    else:
        
        return  D[((sum(n[:a+1])+b-1)%7)] 
      
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
