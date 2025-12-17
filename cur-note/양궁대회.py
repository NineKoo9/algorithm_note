max_diff = 0
answer = [-1]

def solution(n, apeach_info):
    # 전역 변수 초기화를 solution 함수 내에서 해주는 것이 더 안전합니다.
    global max_diff, answer
    max_diff = 0
    answer = [-1]
    
    lion_info = [0] * 11

    def recur_simulate(remain_arrow_cnt, pos, apeach_point, lion_point):
        global max_diff, answer
        
        if pos == 11:
            # 남은 화살이 있다면, 라이언의 점수에는 영향을 주지 않으면서
            # 화살을 모두 소모하기 위해 0점 과녁에 몰아줍니다.
            if remain_arrow_cnt > 0:
                lion_info[10] += remain_arrow_cnt
            
            diff = lion_point - apeach_point

            # 라이언이 이겼을 경우에만 정답 갱신 고려
            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    answer = lion_info[:]
                elif diff == max_diff:
                    # 점수 차가 같다면, 낮은 점수를 더 많이 맞힌 경우로 갱신
                    for i in range(10, -1, -1):
                        if lion_info[i] > answer[i]:
                            answer = lion_info[:]
                            break
                        elif lion_info[i] < answer[i]:
                            break
            
            # 백트래킹: 0점 과녁에 추가했던 화살을 원상 복구
            if remain_arrow_cnt > 0:
                lion_info[10] -= remain_arrow_cnt
            return
        
        # 경우 1: 라이언이 해당 점수를 이기는 경우 (어피치보다 1발 더 쏨)
        arrows_to_win = apeach_info[pos] + 1
        if remain_arrow_cnt >= arrows_to_win:
            lion_info[pos] = arrows_to_win
            recur_simulate(
                remain_arrow_cnt - arrows_to_win, 
                pos + 1, 
                apeach_point, 
                lion_point + (10 - pos)
            )
            lion_info[pos] = 0 # 백트래킹

        # 경우 2: 라이언이 해당 점수를 지는(포기하는) 경우 (0발 쏨)
        next_apeach_point = apeach_point
        if apeach_info[pos] > 0:
            next_apeach_point += (10 - pos)
        
        recur_simulate(remain_arrow_cnt, pos + 1, next_apeach_point, lion_point)
    
    recur_simulate(n, 0, 0, 0)
    return answer

# 이것은 재미나이 풀이
def solution(n, apeach_info):
    # 가장 점수 차가 큰 경우의 라이언 기록과, 그 때의 점수 차를 저장
    answer = [-1]
    max_diff = -1

    # DFS 함수 정의
    # idx: 현재 과녁 점수 (0~10), arrows_left: 남은 화살 수, lion_info: 현재까지 라이언의 기록
    def dfs(idx, arrows_left, lion_info):
        nonlocal max_diff, answer

        # 1. 재귀 종료 조건 (모든 과녁 확인 완료)
        if idx == 11:
            # 남은 화살은 모두 0점 과녁에 사용
            lion_info[10] += arrows_left
            
            # 2. 점수 계산
            lion_score, apeach_score = 0, 0
            for i in range(11):
                if lion_info[i] == 0 and apeach_info[i] == 0:
                    continue
                if lion_info[i] > apeach_info[i]:
                    lion_score += (10 - i)
                else:
                    apeach_score += (10 - i)
            
            # 3. 최고 기록 갱신
            diff = lion_score - apeach_score
            if diff > 0 and diff >= max_diff:
                # 점수 차가 같을 경우, 낮은 점수를 더 많이 맞힌 기록으로 갱신
                # (reversed(lion_info) > reversed(answer)) 트릭으로 간단히 비교 가능
                if diff > max_diff:
                    max_diff = diff
                    answer = lion_info[:]
                else: # diff == max_diff
                    # list를 뒤집어서 비교하면 낮은 점수부터 비교하는 효과
                    if list(reversed(lion_info)) > list(reversed(answer)):
                        answer = lion_info[:]

            # 백트래킹: 0점에 추가했던 화살 원상 복구
            lion_info[10] -= arrows_left
            return

        # 재귀 호출 로직
        # 경우 1: 라이언이 현재 과녁(idx)을 이기는 경우
        arrows_to_win = apeach_info[idx] + 1
        if arrows_left >= arrows_to_win:
            lion_info[idx] = arrows_to_win
            dfs(idx + 1, arrows_left - arrows_to_win, lion_info)
            lion_info[idx] = 0  # 백트래킹: 상태 원상 복구

        # 경우 2: 라이언이 현재 과녁(idx)을 지는 경우 (0발 쏘기)
        dfs(idx + 1, arrows_left, lion_info)

    # 초기 호출
    dfs(0, n, [0] * 11)
    
    return answer