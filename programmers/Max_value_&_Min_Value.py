# my sol
def solution(s):
    arr = s.split()
    new_arr = []
    for i in arr:
        new_arr.append(int(i))

    ans = str(min(new_arr)) + " " + str(max(new_arr))
    return ans
  
# other sol

def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

