class 칠판닦이:
    성격 = "더러움" # 클래스 변수
    def __init__(self, 교실: Classrom):
        self.담당_교실 = 교실
        self.지우개_깨끗함 = 0 # 멤버 변수/ 인스턴스변수
        self.칠판_닦기()

    def 칠판_닦기(self):
        pass # 함수 안의 내용~~


칠판닦이_영수 = 칠판닦이(101호)    # 인스턴스는 클래스로 찍어낸 녀석들
칠판닦이_영수.지우개_깨끗함 = 1

칠판닦이_영희 = 칠판닦이(102호)

칠판닦이_영수.지우개_깨끗함 == 칠판닦이_영희.지우개_깨끗함

칠판닦이.성격 = '깨끗함'

칠판닦이_철수 = 칠판닦이(111)
칠판닦이_철수.성격

칠판닦이_영수.칠판_닦기()



# https://www.youtube.com/watch?v=vrhIxBWSJ04
