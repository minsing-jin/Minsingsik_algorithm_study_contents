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
