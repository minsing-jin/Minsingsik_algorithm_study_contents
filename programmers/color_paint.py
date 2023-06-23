# my sol(답지 인사이트)
def solution(n, m, section):
    last_idx = 1
    ans = 0
    for i in section:
      if i >= last_idx:
        last_idx = i + m
        ans += 1

    return ans
