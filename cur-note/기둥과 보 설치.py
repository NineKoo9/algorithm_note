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
def solution(n, build_frame_lst): # 5 <= N <= 100 build_frame 1000이하
    # 구조물의 상태를 리턴해야한다. 하나 유의할 문제는 x, y, 0은 기둥 1은 보, 0은 삭제 1은 설치
    result = set()
    for build_frame in build_frame_lst:
        x_point, y_point = build_frame[0], build_frame[1]
        frame_type = build_frame[2]
        operation = build_frame[3]
        if operation == 0: # 삭제하는 경우
            result.remove((x_point, y_point, frame_type))
            if destruct_ok(result):
                continue
            else:
                result.add((x_point, y_point, frame_type))
        else:  # 설치하는 경우
            if construct_ok(x_point, y_point, frame_type, result):
                result.add((x_point, y_point, frame_type))
    result = list(result)
    result.sort(key=lambda frame:(frame[0], frame[1], frame[2]))
    return result