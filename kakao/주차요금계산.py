from math import ceil

def solution(fees, records):
    cars = dict()
    for record in records:
        time, num, inout = record.split()
        if inout == 'IN':
            if cars.get(num):
                cars[num][0] = time
            else:
                cars.update({ num: [time, 0] })
        else:
            car = cars[num]
            in_time = car[0]
            in_hour = int(in_time[:2])
            in_min = int(in_time[3:])
            out_hour = int(time[:2])
            out_min = int(time[3:])
            car[1] += (out_hour - in_hour) * 60 + (out_min - in_min)
            car[0] = '23:59'
    sorted_num = sorted(cars.keys())
    answer = []
    for sn in sorted_num:
        car = cars[sn]
        in_time = car[0]
        in_hour = int(in_time[:2])
        in_min = int(in_time[3:])
        parking = car[1] + (23-in_hour) * 60 + (59-in_min)
        fee = fees[1]
        if parking > fees[0]:
            parking -= fees[0]
            fee += fees[3] * ceil(parking/fees[2])
        answer.append(fee)
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# [14600, 34400, 5000]
