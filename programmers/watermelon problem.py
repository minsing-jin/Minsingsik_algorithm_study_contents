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

# 불필요한 메모리 안잡아먹는 code
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)
