def solution(play_time, adv_time, logs):  # logs는 30만 이하
    def to_sec(time):
        h, m, s = int(time[0:2]), int(time[3:5]), int(time[6:8])
        return h * 60 * 60 + m * 60 + s

    def to_time(t):
        ret = ''
        ret += str(t // 3600).zfill(2) + ':'
        t %= 3600
        ret += str(t // 60).zfill(2) + ':'
        t %= 60
        ret += str(t).zfill(2)
        return ret
    # 누적 재생 시간이 가장 큰 구간을 골라야함. 어쨋든 가장 겹치는 시간이 긴 곳
    # 최대 시간은 대략 36만이다.
    play_time = to_sec(play_time)
    adv_time = to_sec(adv_time)
    logs = sorted([(to_sec(log[0:8]), to_sec(log[9:])) for log in logs])
    prefix_sum = [0] * 360001

    # 이제부터 prefix_sum을 기록해나간다. 이건 마치 건물파괴 문제와 비슷하다.
    for start_log, end_log in logs:
        prefix_sum[start_log] += 1
        prefix_sum[end_log + 1] -= 1  # 흠... 다른 사람들도 이 부분 틀리네... 동영상 시청시간이 끝부분을 포함하지 않나봄..?

    # 누적합을 계산해 나간다.
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i - 1] + prefix_sum[i]

    # 가장 많은 시청자가 있는 구간을 찾느다. 이걸 어케 해야할까?
    # 이걸 단순히 합으로 구하면 되는 거였나...?
    mxval, mxtime = sum(prefix_sum[:adv_time]), 0
    curval = mxval
    for i in range(1, 360001 - adv_time):
        curval = curval - prefix_sum[i - 1] + prefix_sum[i + adv_time]
        if curval > mxval:
            mxval = curval
            mxtime = i
    return to_time(mxtime)햇


# 새롭게 푼 풀이.
def solution2(play_time, adv_time, logs):  # logs는 30만 이하
    def sec_to_time(t):
        ret = ''
        ret += str(t//3600).zfill(2)+':'
        t %= 3600
        ret += str(t//60).zfill(2)+':'
        t %= 60
        ret += str(t).zfill(2)
        return ret

    def time_to_sec(t):
        h, m, s = t.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
    
    max_sec = time_to_sec("99:59:59") + 10
    # user_count[i]는 [i - 1, i) 구간에 있는 유저의 수
    user_count = [0 for _ in range(max_sec)]
    sec_logs = [tuple(map(time_to_sec, log.split("-"))) for log in logs]
    for start_sec, end_sec in sec_logs:
        user_count[start_sec + 1] += 1
        user_count[end_sec + 1] -= 1
    
    # 누적합을 진행하여 구간별 인원을 구한다.
    for i in range(1, max_sec):
        user_count[i] += user_count[i - 1]
    
    # 누적합을 한번더 진행하여 [0, i) 구간의 누적 재생 시간을 구한다.
    prefix_play_sum = [0 for _ in range(max_sec)]
    for i in range(1, max_sec):
        prefix_play_sum[i] = prefix_play_sum[i - 1] + user_count[i]
    
    # 이제부터 재생 시간 구간이 움직이면서 어떤 구간에 가장 많은지 구한다.
    adv_play_length = time_to_sec(adv_time)
    max_value = 0
    answer = 0
    for start_sec in range(max_sec - adv_play_length):
        # [start_time, end_ad_time) 이 구간에서 총 재생시간을 구한다.
        total_sec = prefix_play_sum[start_sec + adv_play_length] - prefix_play_sum[start_sec]
        if total_sec > max_value:
            max_value = total_sec
            answer = start_sec
    return sec_to_time(answer)
            
        
        
    
    