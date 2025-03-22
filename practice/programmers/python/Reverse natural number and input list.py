# my sol
def solution(n):
    return int(''.join(sorted(str(n), reverse = True)))
  
# other sol
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
  
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]
