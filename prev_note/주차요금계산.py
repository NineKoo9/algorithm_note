def solution(fees, records):
    from collections import defaultdict
    import math
    
    END_TIME = 23 * 60 + 59
    default_time, default_fee, unit_time, unit_fee = fees
    car_total_dic = defaultdict(int)
    for record in records:
        time, car_num, status = record.split(" ")
        time = int(time[0:2]) * 60 + int(time[3:5])
        if status == "IN":
            car_total_dic[car_num] += (END_TIME - time)
        else:
            car_total_dic[car_num] = time - END_TIME + car_total_dic[car_num]
    result = sorted(list(car_total_dic.items()), key=lambda x:x[0])
    return [default_fee + unit_fee * math.ceil((value - default_time) / unit_time) if value > default_time else default_fee for key, value in result]    
