# 문제 출처: https://wikidocs.net/7041

class 차:
  # super class
  def __init__(self, 바퀴, 가격):
    self.바퀴 = 바퀴
    self.가격 = 가격

  def 정보(self):
    print('바퀴수 ', self.바퀴)
    print('가격 ', self.가격)
    



class 자전차(차):
  # sub class
  def __init__(self, 바퀴, 가격, 구동계):
    self.바퀴 = 바퀴
    self.가격 = 가격
    self.구동계 = 구동계

  def 정보(self):
    super().정보()    # super class의 정보 메서드를 불러옴.
    print('구동계 ', self.구동계)




# 285 my solution
# class 자동차(차):
#   # sub class2
#   def 정보(self):
#     print(f'바퀴수 {self.바퀴}')        # sub class는 super class를 참조하므로 self에 저장되어있는 녀석들을 sub calss에서 그대로 불러올 수 있다.
#     print(f'가격 {self.가격}')

# 285 답지 solution
class 자동차(차):
    # sub class 2
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)    # super() 라는 함수는 super class 즉, 부모클래스의 임시적인 객체를 반환하여 부모클래스의 메소드를 사용할 수 있게 하는 것 입니다.
                                        # Class 선언 내부에서 super를 호출하면, 인자 전달을 따로 하지 않아도 자동으로 해당 클래스의 부모 클래스를 호출해줍니다.
                                        # inheritance 관계에서 inheritance 대상인 super class를 호출하는 함수임!
                                        # super()의 인자로는 두 개가 전달되며, 하위클래스의 이름과 하위클래스의 객체(object)가 필요합니다.
                                        # 상속을 받게 된다면 super class의 메서드를 sub class로 선언된 인스턴스에서 사용할 수 있음!
    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)

'''
281번 클래스 정의
car = 차(2, 1000)
print(car.바퀴)
print(car.가격)
'''

'''
283번 class inheritance
bicycle = 자전차(2, 100)
print(bicycle.가격)
'''

'''
284번 class inheritance
bicycle = 자전차(2, 100, "시마노")
print(bicycle.구동계)

'''


'''
285번 class
car = 자동차(4, 1000)
car.정보()
'''

'''
286번 부모클래스 생성자 호출: 다음 코드가 동작하도록 차 클래스를 수정하세요.
bicycle = 자전차(2, 100, "시마노")
bicycle.정보()
'''

'''
287번 부모 클래스 메서드 호출
bicycle = 자전차(2, 100, "시마노")
bicycle.정보()
'''

'''
288 메서드 오버라이딩: 다음 코드의 실행 결과를 예상해보세요.
class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()

정답: 자식 호출    
'''

'''
289 생성자: 다음 코드의 실행 결과를 예상해보세요.
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
나 = 자식()

정답: 자식생성
'''
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

'''
290 부모클래스 생성자 호출: 다음 코드의 실행 결과를 예상해보세요.
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

정답: 자식생성, 부모생성
'''

# 잘 설명되어있는 super 사용법 및 설명: https://supermemi.tistory.com/178
