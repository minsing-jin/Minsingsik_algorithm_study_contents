# 1. 첫 람다 사용 해결! neis!!

def solution(A,B):
    ans = 0
    A.sort()
    B.sort(reverse = True)
    ans += int(sum(map((lambda x,y: x*y),A,B)))

    return ans
  
  
--------------------------------------

def solution(A,B):

    return int(sum(map((lambda x,y: x*y),sorted(A),sorted(B,reverse = True))))
  
---------------------------------------

# other sol

def getMinSum(A,B):
  return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))

--------------------------------------------

# 효율성 문제로 폐기

def solution(A,B):
#    tmp = A + B  ->  한꺼번에 이러면 A에 중복된 min과 max가 곱해질 수 있음
    ans = 0
    cnt = len(A)
    for i in range(cnt):
        if max(A) < max(B):
            ans += (max(B) * min(A))
            B.remove(max(B))
            A.remove(min(A))
            print(ans)

        elif max(A) == max(B):
            if min(A) < min(B):
                ans += (max(B) * min(A))
                B.remove(max(B))
                A.remove(min(A))
                print(ans)
            elif min(A) > min(B):
                ans += (min(B) * max(A))
                B.remove(min(B))
                A.remove(max(A))

                print(ans)
            else:
                ans += (min(B) * max(A))
                B.remove(min(B))
                A.remove(max(A))
            
    #         elif min(A) == min(B): # A와 B의 min max가 같을때

        else:
            ans += (min(B) * max(A))
            B.remove(min(B))
            A.remove(max(A))

    
    return ans
