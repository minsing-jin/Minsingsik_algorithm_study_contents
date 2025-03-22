# my sol
def solution(nums):
    tmp = list(set(nums))

    if len(nums)//2 <= len(tmp):
        return len(nums)//2
    else:
        return len(tmp)
   
# other sol
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
