# 출처: https://wikidocs.net/7037

import random

class Account:
    acc_cnt = 0

    def __init__(self, account_H, balanced):        # 생성자(constructor): 맨처음 초기 생성
        self.account_H = account_H
        self.balanced = balanced
        
        self.bank = 'SC은행'
        self.account_num = str(random.random())[2:5] + '-' + str(random.random())[5:7] + '-' + str(random.random())[5:11]
        
        '''
        계좌 번호 랜덤 생성 답지 풀이
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-0
        '''
        Account.acc_cnt += 1


    @classmethod                       # 메서드: class 안의 함수들
    def get_account_num(cls):         # 클래스 메소드 (class method) : cls로 클래스 필드에 접근하는 메소드이며, 정적 메소드처럼 @classmethod라고 메소드 선언 앞에 표기해야 한다.
      print(cls.acc_cnt)          # 클래스 변수:  클래스 내부에 선언된 변수, 일반적인 변수와 동일한 형태


    def deposit(self,deposit_won):
      if deposit_won >= 1:
        if Account.acc_cnt == 5:
          self.balanced += deposit_won
          self.balanced *= 1.01

        else:
          self.balanced += deposit_won   # self 주소의 balanced의 주소에 계속해서 입금 금액 더하기
      Account.acc_cnt = 0


    def withdraw(self, withdraw_won):       # self 주소의 withdraw_won 의 주소에 계속해서 출금 금액 빼기 / construtor에 있는 변수들을 사용할 경우에는 global variable이 아니므로 주소로 접근해야함. 따라서 self를 붙여서 접근
      if self.balanced >= withdraw_won:      # 따라서 메서드를 인스턴스 메서드는 인스턴스 필드(클래스에 저장되어있는 변수) 영역으로 진입할 수 있음. 클래스에 저장되어있는 변수들을 마음껏 사용할 수 있다. 그래서 처음에 self를 붙이는 거임. 인스턴스 메서드의 인스턴스 필드의 클래스 변수들을 사용하려고!
        self.balanced -= withdraw_won
      else:
        print("Balance is insufficient")


    '''
    def display_info(self):
      print("은행이름: ", self.bank)
      print("예금주: ", self.account_H)
      print("계좌번호: ", self.account_num)
      print("잔고: ", f"{self.balanced:,}")  # f-string에서 : 변수 다음에 : 다음에 콤마를 찍으면 3자리수마다 콤마
'''

    def display_info(self):
      print('은행이름: ' + self.bank)
      print('예금주: ' + self.account_H)
      print('계좌번호: ' + self.account_num)
      print("잔고: ", f"{self.balanced:,}")  # f-string에서 : 변수 다음에 : 다음에 콤마를 찍으면 3자리수마다 콤마
      
      # 실패 코드 다시 시도할것
      # tmp = str(self.balanced)
      # cnt = 0

      # for i in tmp:
      #   if len(tmp) > 3:
      #     if i%3 == 0:
      #       tmp = tmp[:i] + ',' + tmp[i:]
      #       print(tmp)
      #   else:
      #     break
      # print('잔고: ' + tmp + '원')





# self는 왜 붙이는건가? self는 무엇인가? bank에는 왜 self를 붙이는가?
kim = Account("김민수", 100)
lee = Account("이민수", 100)
'''
271. Account 클래스
print(kim.account_H)
print(kim.balanced)
print(kim.bank)
print(kim.account_num)
'''

'''
272. 클래스 변수
print(Account.acc_cnt)
print(Account.acc_cnt)
kim.get_account_num()
'''

'''
274 입금 메서드/출금 메서드
k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
'''

# k = Account("kim", 100)
# k.deposit(100)
# k.withdraw(90)
# k.display_info()

p = Account("파이썬", 1000)
p.display_info()






# 277 번부터 시작 이자 붙이는 코드 구현 할것
