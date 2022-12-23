# my sol
from itertools import combinations, permutations
def solution(nums):
    ans = 0
    combi = list(combinations(nums, 3))
    for i in combi:
        for x in range(2,sum(i)):

            if sum(i)%x == 0:

                break
            if x == sum(i)-1:
                ans += 1
                break
    return ans
  
  
# other sol
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
  
  

# 에라토네스의 체 방식
def sieve(n):
    """
    에라토스테네스의 체
    """
    if n < 2:
        return []

    #[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    s = [0, 0] + [1] * (n - 1)

    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return [i for i, v in enumerate(s) if v]

def solution(nums):
    primes = sieve(3000)

    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) in primes:
                    count += 1

    return count
