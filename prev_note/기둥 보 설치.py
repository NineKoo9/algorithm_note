def is_ok(result, build_frame):
    # 여기서 현재 프레임에서 build_frame을 설치할 수 있는지 없는지 체크해야한다.
    build_pos = [build_frame[0], build_frame[1]]  # x, y
    frame_type, operation = build_frame[2], build_frame[3]
    if frame_type == 0:  # 기둥인경우
        if build_pos[1] == 0:  # 바닥에 있거나?
            return True  # 그러면 ok
        else:  # 바닥이 아니라면 기존의 프레임과 따져봐야지
            for current_frame in result:
                current_frame_pos = [current_frame[0], current_frame[1]]
                current_frame_type = current_frame[2]
                if current_frame_type == 0:  # 기존의 프레임이 기둥인경우
                    # 다른 기둥 위에 있어야한다.
                    if current_frame_pos[0] == build_pos[0] and current_frame_pos[1] + 1 == build_pos[1]:
                        return True
                else:  # 기존 프레임이 보인 경우
                    # 한쪽 끝부분위에 있어야한다.
                    if current_frame_pos[0] == build_pos[0] and current_frame_pos[1] == build_pos[1]:
                        return True
                    elif current_frame_pos[0] + 1 == build_pos[0] and current_frame_pos[1] == build_pos[1]:
                        return True
            return False

    else:  # 설치할려는 것이 "보"인경우
        for idx, current_frame in enumerate(result):
            current_frame_pos = [current_frame[0], current_frame[1]]
            current_frame_type = current_frame[2]
            if current_frame[2] == 0:  # 기존 프레임이 기둥인경우
                # 한쪽 끝 부분이 기둥 위에 있어야 한다.
                if current_frame_pos[0] == build_pos[0] and current_frame_pos[1] + 1 == build_pos[1]:
                    return True
                elif current_frame_pos[0] == build_pos[0] + 1 and current_frame_pos[1] == build_pos[1] - 1:
                    return True
            else:  # 기존 프레임이 보인경우
                if build_pos[0] + 1 == current_frame_pos[0] and build_pos[1] == current_frame_pos[1]:
                    # 반대쪽도 맞춰줘야하니까...
                    for idx2, current_frame2 in enumerate(result):
                        if idx == idx2:
                            continue
                        current_frame_pos2 = [current_frame2[0], current_frame2[1]]
                        current_frame_type2 = current_frame2[2]
                        if current_frame_type2 == 1 and build_pos[0] - 1 == current_frame_pos[0] and build_pos[1] == \
                                current_frame_pos[1]:
                            return True
        return False


def solution(n, build_frame_lst):  # 5 <= N <= 100 build_frame 1000이하
    # 구조물의 상태를 리턴해야한다. 하나 유의할 문제는 x, y, 0은 기둥 1은 보, 0은 삭제 1은 설치
    result = []
    for build_frame in build_frame_lst:
        typ = build_frame[3]
        if typ == 1 and is_ok(result, build_frame):
            result.append([build_frame[0], build_frame[1], build_frame[2]])
    return result

# 여기서 부터 새로운 풀이... 질문목록을 보긴했다...
# 관점을 다르게 잡았어야 했다... 현재 무엇을 설치할려면 주위와의 연관관계를 하나하나 따졌는데... 설치하기 위한 다른 프레임이 존재하는 가? 로 갔어야했다...

def destruct_ok(result):
    # 삭제를 만족하는지는 어케하지?
    # 역시 반복문을...
    for x_point, y_point, frame_type in result:
        if not construct_ok(x_point, y_point, frame_type, result):
            return False
    return True


def construct_ok(x_point, y_point, frame_type, result):
    if frame_type == 0:  # 기둥인 경우
        if y_point == 0 \
                or (x_point, y_point, 1) in result \
                or (x_point - 1, y_point, 1) in result \
                or (x_point, y_point - 1, 0) in result:
            return True
        else:
            return False
    else:  # "보"인 경우
        if (x_point, y_point - 1, 0) in result \
                or (x_point + 1, y_point - 1, 0) in result \
                or ((x_point + 1, y_point, 1) in result and (x_point - 1, y_point, 1) in result):
            return True
        else:
            return False


# 하... 이 문제... 시간 복잡도를 너무 신경쓴걸까...
def solution(n, build_frame_lst):  # 5 <= N <= 100 build_frame 1000이하
    # 구조물의 상태를 리턴해야한다. 하나 유의할 문제는 x, y, 0은 기둥 1은 보, 0은 삭제 1은 설치
    result = set()
    for build_frame in build_frame_lst:
        x_point, y_point = build_frame[0], build_frame[1]
        frame_type = build_frame[2]
        operation = build_frame[3]
        if operation == 0:  # 삭제하는 경우
            result.remove((x_point, y_point, frame_type))
            if destruct_ok(result):
                continue
            else:
                result.add((x_point, y_point, frame_type))
        else:  # 설치하는 경우
            if construct_ok(x_point, y_point, frame_type, result):
                result.add((x_point, y_point, frame_type))
    result = list(result)
    result.sort(key=lambda frame: (frame[0], frame[1], frame[2]))
    return result