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


def solution(play_time, adv_time, logs):  # logs는 30만 이하
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
    return to_time(mxtime)



