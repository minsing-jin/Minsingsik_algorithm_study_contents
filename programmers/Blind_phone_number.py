```python
#문제 : phone_number 값이 들어오면 뒷자리 4자리만 빼고 모두 *로 보안

# 나의 ㅈ밥 풀이
def solution(phone_number):

    protect = ''
    prot_num = phone_number[:-4]
    for i in range(len(prot_num)):
        protect += '*'
    answer = phone_number.replace(prot_num, protect)


    return answer
-----------------------------------------------------------


# 지리는 풀이
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

```
