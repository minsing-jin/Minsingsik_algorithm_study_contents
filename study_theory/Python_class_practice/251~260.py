# 251 클래스, 객체, 인스턴스
'''
클래스: 모음집
객체: 붕어빵틀
인스턴스: 붕어빵
'''

# 252 클래스 정의
class Human:
    pass
 
# 253 인스턴스 생성
class Human:
    pass

areum = Human()


# 254 클래스 생성자-1
class Human:
    def __init__(self):
        print("응애응애")
    
areum = Human()

# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

class Human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    

areum = Human("아름", 25, "여자")
print(areum.name)

# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
class Human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    

areum = Human("아름", 25, "여자")
print(areum.name)

# 257 클래스 메소드 - 1
class Human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
    

areum = Human("아름", 25, "여자")
areum.who()

# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.

class Human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
        
    def setInfo(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        
    
areum = Human("불명", "미상", "모름") # 디폴트 상태 만들기
areum.who()      # Human.who(areum)

areum.setInfo("아름", 25, "여자") # 입력값에 따른 출력물들 만들기
areum.who()      # Human.who(areum)





# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
class Human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        
    def __del__(self):
        print("나의 죽음을 알리지 말라")
        
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
        
    def setInfo(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    
    
areum = Human("아름", 25, "여자")
del areum




# 260 에러의 원인
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.

class OMG : 
    def print() :
        print("Oh my god")

>>> >>> myStock = OMG()
>>> myStock.print()
TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()

TypeError: print() takes 0 positional arguments but 1 was given
  
 


class OMG :
    def print(self) :
        print("Oh my god")


mystock = OMG()
mystock.print()      # OMG.print(mystock)


문제 출처: https://wikidocs.net/7035
