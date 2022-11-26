# 261 Stock 클래스 생성
class Stoke:
    pass
 


# 262 생성자
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
      
      
삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)     




# 263 메서드
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name
    
a = Stock(None, None)
a.set_name("삼성전자")  # Stock.set_name(a, "삼성전자")
print(a.name)


 

# 264 메서드
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name
        
    def set_code(self, code):
        self.code = code
        
a = Stock(None, None)
a.set_code("005930")
print(a.code)


# 265 메서드
class Stock:
    def __init__(self,name, code):
        self.name = name
        self.code = code
    
    def set_code(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
삼성 = Stock("삼성전자", "005930")
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.



----------------------------------------------------------------------------------------------------------------------------


# 266 - 270
'''
1. 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입입니다.

2. 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.
항목	정보
종목명	삼성전자
종목코드	005930
PER	15.79
PBR	1.33
배당수익률	2.83

3. PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.

4. 267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.

5. 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.\

종목명	종목코드	PER	PBR	배당수익률
삼성전자	005930	15.79	1.33	2.83
현대차	005380	8.70	0.35	4.27
LG전자	066570	317.34	0.69	1.37
'''

class Stock:
    def __init__(self,name, code, PER, PBR, dividend_yield):   # 초기 constructor(생성자)로서 처음 한번만 실행하는 녀석/ 저장하는 self 변수들도 마찬가지
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.dividend_yield = dividend_yield
        
    def set_code(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code      # 메서드 안에 내장된 변수 field에 입력받은 code attribute 저장
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
    def set_per(self, PER):
        self.PER = PER
    
    def set_pbr(self, PBR):
        self.PBR = PBR
        
    def set_dividend(self, dividend_yield):
        self.dividend_yield = dividend_yield
        
        

삼성전자 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69,1.37)

삼성전자.set_per(12.75)
print(삼성전자.PER)

lst = [삼성전자,현대차,LG전자]

for i in lst:
    print(f'{i.code} PER: {i.PER}')

