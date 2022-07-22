# my sol
def solution(n):
    tmp = []
    for i in range(1, n+1):
        if i%2 != 0:
            tmp.append('수')
        else:
            tmp.append('박')


    return ''.join(tmp)
  
# other sol
def water_melon(n):
    s = "수박" * n
    return s[:n]
