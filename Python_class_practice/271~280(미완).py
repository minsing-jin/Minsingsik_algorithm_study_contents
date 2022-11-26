# 출처: https://wikidocs.net/7037

import random

class Account:
    def __init__(self, account_H, balanced):        # 생성자(constructor): 맨처음 초기 생성
        self.account_H = account_H
        self.balanced = balanced
        
        self.bank = 'SC은행'
        self.account_num = str(random.random())[2:5] + '-' + str(random.random())[5:7] + '-' + str(random.random())[5:11]
        
        # 0으로도 시작할 수있게 ㄲ
        

                          # 메서드: class 기능들
            # self는 왜 붙이는건가? self는 무엇인가? bank에는 왜 self를 붙이는가?
kim = Account("김민수", 100)
print(kim.account_H)
print(kim.balanced)
print(kim.bank)
print(kim.account_num)

# 다시다시!
