# my sol
def solution(n):
    for i in range(1,n+1):
        if n%i == 1:
         return i
         
         
# other people sol
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]
Footer
