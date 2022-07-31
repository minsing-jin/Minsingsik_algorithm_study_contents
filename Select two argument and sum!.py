# my sol
from itertools import *

def solution(numbers):
    printList = list(combinations(numbers, 2))
    tmp = []

    for i in printList:
        tmp.append(sum(i))

    tmp = list(sorted(set(tmp))) 
    return tmp
  
# other sol
from itertools import combinations
def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))

# for문 이용
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
