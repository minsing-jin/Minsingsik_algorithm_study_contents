fees = [180, 5000, 10, 600] 
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
'''
fee[0] = 기본시간(분)
fee[1] = 기본요금(원)
fee[2] = 단위 시간(분)
fee[3] = 단위 요금(원)
'''

time = []
car_num = []
status = []
info = []
for i in records:
    info.append(i.split())

info = sorted(info, key=lambda x: x[1])



for n in info:
    print(n)
    time.append(n[0])
    car_num.append(n[1])
    status.append(n[2])
tmp = list(set(car_num))
car_kind = {key: value for key, value in dict.fromkeys(tmp).items()}

cnt = 0
# time을 딕셔너리에 저장하기/ 아니면 그냥 records만으로 해결할수있나?
for i in car_kind:
    car_kind[i] = [time,car_num.count(i)] 
print(car_kind)  

cnt = 0
for i in car_kind[1]: # 각 차량 종류가 왔다 갔다한 횟수
    cnt += i
    if i%2 != 0:
        for n in range(i):
            time[]
        
        
    

print(type(tmp))

#print(time)
print(car_kind)
#print(status)

#ele_cnt = {key: value for key, value in dict.fromkeys(car)}

# print(info)
