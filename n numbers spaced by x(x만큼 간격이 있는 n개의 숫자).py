#  my solution
# def solution(x, n):
    
#     real_x = x
#     answer = []
#     for i in range(n):
        
#         answer.append(x)
#         x += real_x
    
    
#     return answer



# fucking easy solution
def solution(x, n):
    
    return [i * x + x for i in range(n)]
