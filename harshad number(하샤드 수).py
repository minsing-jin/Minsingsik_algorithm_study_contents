# 예를 들어 18의 자릿수 합은 1+8=9이고, 
# 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수,
# solution을 완성해주세요

# my solution 1
"""
def solution(x):

    final_cal = 0
    mid_cal = [int(i) for i in str(x)]
    for i in range(len(mid_cal)):
        final_cal += mid_cal[i]
    if x%final_cal == 0:
        return True
    else:
        return False
        """
        
# my solution 2
'''

def solution(x):
    final_cal = 0
    mid_cal = sum([int(i) for i in str(x)])


    if x%mid_cal == 0:
        return True
    else:
        return False
        
        '''


# easy code

def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0
