# my sol
def solution(n, arr1, arr2):
    real1 = []
    real2 = []

    # 이진수 변환 코드

    # arr1 이진수 변환
    for i in arr1: # 요소 하나하나 꺼내기
        tmp1 = [0 for x in range(n)]
        cnt = 0
        while True:  
            if i > 1:
                tmp1[cnt] = i - ((i//2)*2)
                i = i//2
                cnt += 1
            else:
                tmp1[cnt] = i
                tmp1.reverse()
                real1.append(tmp1)
                cnt = 0
                break

    # arr2 이진수 변환
    for i in arr2: # 요소 하나하나 꺼내기
        tmp1 = [0 for x in range(n)]
        cnt = 0
        while True:  
            if i > 1:
                tmp1[cnt] = i - ((i//2)*2)
                i = i//2
                cnt += 1
            else:
                tmp1[cnt] = i
                tmp1.reverse()
                real2.append(tmp1)
                cnt = 0
                break



    real = real1

    # 자릿수 해독
    for i in range(n): # real1와 real2 row 지정
        row1 = real1[i]
        row2 = real2[i]

        for x in range(n): # row1과 row2의 값 비교 

            if row1[x] + row2[x] >= 1:
                real[i][x] = 1
            else:
                real[i][x] = 0

    # 1은 #으로 변환, 0은 " "로 변환

    # 모든 요소에 대해서 접근
    for i in range(n):
        for x in range(n):
            if real[i][x] == 1:
                real[i][x] = "#"
            else:
                real[i][x] = " "

    for i in range(n):
        real[i] = "".join(real[i])

    return real

  
# other sol
# 1
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
# -> zip으로 두 array 묶고, bin함수로 두녀석을 binary로 바꾸고 str로 바꿈. rjust로 옆에부터 결과값을 계속 붙임. 그리고 replace로 1이면 , 0이면 공백으로 변환
# 불필요한 반복 없이 한꺼번에 arr두개를 처리했음. sota!

# 2
solution = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])
# zfill() -> 문자열 앞 0으로 채우기
# zip으로 묶은 다음 그 둘중 하나가 1이라면 #으로 채우기
