# my sol
def solution(fees, records):
    time = []
    car_num = []
    status = []
    info = []
    for i in records:   # Split time, car number, car state by blank and append info array
        info.append(i.split())

    info = sorted(info, key=lambda x: x[1]) # Arrange based car number ordered by small number

    for n in info:
        time.append(n[0])
        car_num.append(n[1])
        status.append(n[2])



    # Delete overlap car number
    tmp = list(set(car_num))  
    car_kind = dict(sorted({key: value for key, value in dict.fromkeys(tmp).items()}.items()))

    print(car_kind)

    tmp2 = []
    tmp_num = 0

    # Convert time to minute
    for i in time:
        idx = time.index(i)
        i = i.split(sep = ":")
        i[0] = int(i[0]) * 60
        i[1] = int(i[1])
        time[idx] = sum(i)


    cnt = 0
    mul = 0

    # Storing time in car_kind dictionary and settle parking bill
    for i in car_kind:
        cnt += car_num.count(i)
        car_kind[i] = time[cnt-(car_num.count(i)): cnt]
        if len(time[cnt-car_num.count(i): cnt])%2 != 0: # If car status doesn't end out, add 23:59
            car_kind[i].append(1439)

        aacc_parking_fee_tmp = [] # accumulate parking fee

        # Settle parking bill
        for n in range(int(len(car_kind[i])/2)):
            aacc_parking_fee_tmp.append(car_kind[i][(n*2)+1] - car_kind[i][(n*2)])
            print(aacc_parking_fee_tmp)
        if sum(aacc_parking_fee_tmp) <= fees[0]:
            car_kind[i] = fees[1]
        else:
            if (sum(aacc_parking_fee_tmp) - fees[0])% fees[2] != 0:
                car_kind[i] = fees[1] + (int((sum(aacc_parking_fee_tmp) - fees[0])/fees[2])+1)*fees[3]  # rounds parking time if parking time doesn't fall apart unit time
            else:
                car_kind[i] = fees[1] + ((sum(aacc_parking_fee_tmp) - fees[0])/fees[2])*fees[3]





    ans = []
    for i in car_kind:
        ans.append(car_kind[i])



    # 누적 주차시간으로 고려
    return ans



'''
------------------------------------------------------------------------------------------------------------------------
'''

# other sol

from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False
        if self.in_flag:  self.in_time = str2int(t)
        else:             self.total  += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]
