# my sol
def solution(ingredient):
    lst_ingredient = ingredient
    # ingredient = [str(i) for i in ingredient]
    # str_ingredient = ''.join([s for s in ingredient])
    detector = [1,2,3,1]
    ans = 0


    n = 0
    while True:
        try:

            if lst_ingredient[n] == detector[0]:

                if lst_ingredient[n+1] == detector[1]:

                    if lst_ingredient[n+2] == detector[2]:

                        if lst_ingredient[n+3] == detector[3]:

                            ans += 1

                            del lst_ingredient[n:n+4]


                            n = n-4 # 앞에 있는 새로운 녀석과 합쳐졌을때 새로운 1231이 나올때를 대비해서 1231 detector의 길이만큼 ㅏㅍ으로 빼냄
                        else:
                            n += 1
                    else:
                        n += 1
                else:
                    n += 1
            else:
                n += 1
        except:
            break


    return ans


# 빵/야채/고기/빵 순서가 필수
#   1  2   3   1 -> 배열 순서를 찾을것! 

# 효율성 이슈: https://brownbears.tistory.com/452  -> 리스트 슬라이싱 했을때 상당히 많은 시간이 걸림 따라서 del을 사용함!



# other sol
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt

  
def solution(ingredient):
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)
        while s[-4:] == [1, 2, 3, 1]:
            s.pop()
            s.pop()
            s.pop()
            s.pop()
            answer += 1

    return answer
