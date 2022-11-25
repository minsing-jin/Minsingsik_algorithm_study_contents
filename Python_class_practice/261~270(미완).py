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


# 265 265 메서드
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.
