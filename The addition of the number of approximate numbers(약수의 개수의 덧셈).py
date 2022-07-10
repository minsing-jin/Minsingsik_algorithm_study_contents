```Python
# my solution
def solution(left, right):
    lst = []
    ans = 0

    for i in range(left,right+1):
        for n in range(1,i+1):

            if i % n == 0:
                lst.append(n)

        if len(lst)%2 == 0:
            ans += i
            lst = []

        elif len(lst)%2 != 0:
            ans -= i
            lst = []
    return ans
    
# other people solution
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
   # 제곱수(^0.5)는 약수의 개수가 홀수임! 이걸 이용해서 코딩 한것~
```
