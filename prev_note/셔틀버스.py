from collections import deque


def answer_format(t):
    hour = t // 60
    minute = t % 60
    answer = (str(hour) if len(str(hour)) == 2 else "0" + str(hour)) + ":" + (
        str(minute) if len(str(minute)) == 2 else "0" + str(minute))
    return answer


def solution(N, t, m, timetable):  # 09시부터 N회, t분간격, m명이 최대 탑승
    total_crew = len(timetable)
    crew_time_table = deque(sorted([int(crew_time[0:2]) * 60 + int(crew_time[3:5]) for crew_time in timetable]))
    # 최대한 늦게라는 점에서... 모든 timetable을 다 탐색한 이후에야 콘의 출근시간을 정할 수 있겠다.
    # 아닐지도? 적당한 부분에서 예외처리를 해줄필요는 있다.
    first_bus_time = 60 * 9
    for n in range(N):
        stack = []
        bus_time = first_bus_time + n * t
        for _ in range(m):  # m명이 탈 수 있으니까...
            if crew_time_table and crew_time_table[0] <= bus_time:
                stack.append(crew_time_table.popleft())
            elif not crew_time_table:  # 이까지 왔다는 것은 아직 더 탈수있는데 모두 태웠단 것이니까
                corn_time = bus_time
                return answer_format(corn_time)
    # 여기까지 왔으면 버스는 모두 운행한 것이다. 남아있는 사람이 있을 수 있지만...
    # 자 그렇다면... 버스는 모두 운행했고.. 탑승한 승객은 있을수잇고 없을 수 있다.
    # 잇다면? 마지막 승객 뒤에 타야하나 앞에 타야하냐? 위에서 걸러냈으니까 앞에 타야한다.
    # 없다면? 마지막 버스타임에 타야한다.
    # 만약에 탑승한 승객수보다 운행한 버스에 자리가 남아있다면?
    if stack:
        corn_time = stack[-1] - 1
    elif stack and len(stack) < m:
        corn_time = bus_time
    else:
        corn_time = bus_time
    return answer_format(corn_time)

# print(solution(3, 1, 2, ["06:00", "23:59", "05:48", "00:01", "00:01"]))