# my solution
def solution(numbers):
    tmp = [i for i in range(10)]
    [tmp.remove(i) for i in numbers]


    return sum(tmp)
  
# other easy solution

#1
def solution(numbers):
    return 45 - sum(numbers)
  
  
#2
solution = lambda x: sum(range(10)) - sum(x)
