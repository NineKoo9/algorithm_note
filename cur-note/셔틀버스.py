def binary_right(arr, n):
    ans = len(arr)
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= n:
            start = mid + 1
        elif arr[mid] > n:
            ans = mid
            end = mid - 1
    return ans

def solution(n, t, m, timetable):
    co_arrive_times = sorted(list(map(lambda s: int(s[:2]) * 60 + int(s[3:]), timetable)))
    max_possible_time = 0
    for corn_arrive_time in range(0, 24 * 60):
        # 콘이 특정시간에 왔을때 버스를 탈 수 있냐 없냐를 체크하면 될듯한데?
        corn_arrive_order = binary_right(co_arrive_times, corn_arrive_time)
        # 콘이 corn_arrive_order번째로 서있을 때 버스를 탈 수 있냐 없냐를 다 체크하자.
        p = -1
        for bus_arrive_time in range(540, 540 + n * t, t):
            onboard_count = 0
            for _ in range(m):
                if p + 1 < len(co_arrive_times) and co_arrive_times[p + 1] <= bus_arrive_time:
                    p += 1
                    onboard_count += 1
            # 이제 p번까지 탈 수 있는데 그 안에 콘이 들어있다면? ok이다.
            # 또는 빈자리가 남아있고 콘이 버스도착시간 이하에 도착했어도 ok이다.
            if corn_arrive_order <= p or (onboard_count < m and corn_arrive_time <= bus_arrive_time):
                max_possible_time = max(max_possible_time, corn_arrive_time)
            
    hour = str(max_possible_time // 60).zfill(2)
    minute = str(max_possible_time % 60).zfill(2)
    return hour + ":" + minute
        
#### 아래는 처음의 풀이

from collections import deque

def answer_format(t):
    hour = t // 60
    minute = t % 60
    answer = (str(hour) if len(str(hour)) == 2 else "0" + str(hour)) + ":" + (str(minute) if len(str(minute)) == 2 else "0" + str(minute))
    return answer
    
def solution(N, t, m, timetable): # 09시부터 N회, t분간격, m명이 최대 탑승
    total_crew = len(timetable)
    crew_time_table = deque(sorted([int(crew_time[0:2]) * 60 + int(crew_time[3:5]) for crew_time in timetable]))
    first_bus_time = 60 * 9
    for n in range(N):
        stack = []
        bus_time = first_bus_time + n * t
        for _ in range(m): # m명이 탈 수 있으니까...
            if crew_time_table and crew_time_table[0] <= bus_time:
                stack.append(crew_time_table.popleft())
            elif not crew_time_table: # 이까지 왔다는 것은 아직 더 탈수있는데 모두 태웠단 것이니까
                corn_time = bus_time
                return answer_format(corn_time)
    # 이것은 마지막 버스에 탄 사람들 일것이다. 당연히 m명 이하일 것이다.
    if stack:
        corn_time = stack[-1] - 1
    else: # 마지막 버스에 아무도 안탔다면?
        corn_time = bus_time
    return answer_format(corn_time)
    