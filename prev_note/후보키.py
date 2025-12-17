from itertools import combinations


def is_unique(relation, candidate_key):
    print("is_uniqe", candidate_key)
    total_row = len(relation)
    total_column = len(relation[0])
    row_set = set()
    for i, row in enumerate(relation):
        temp = []
        for k in candidate_key:
            temp.append(relation[i][k])
        row_set.add(tuple(temp))
    return len(row_set) == total_row


def is_minimal(valid_keys, candidate_key):
    for valid_key in valid_keys:
        if all(c in candidate_key for c in valid_key):
            return False
    return True


def solution(relation):
    # 원하는 것은 후보키의 갯수다.
    total_row = len(relation)  # 1 ~ 20
    total_column = len(relation[0]) + 1  # 이야... 여기서 total_column 이거 잘못체크해서... 전체 컬럼이 후보키인 경우를 고려못했네...

    candidate_key_list = []
    for i in range(1, total_column):
        candidate_key_list += list(combinations(range(total_column - 1), i))
    print(candidate_key_list)
    valid_keys = []
    for idx, candidate_key in enumerate(sorted(candidate_key_list, key=lambda a: len(a))):
        # 최소성 확인
        if not is_minimal(valid_keys, candidate_key):
            continue
        if is_unique(relation, candidate_key):
            valid_keys.append(candidate_key)
    return len(valid_keys)

# 이건 잘못된 풀이였는데... Idx + 1 로 고쳤다...
def solution(relation):
    # 원하는 것은 후보키의 갯수다.
    total_column = len(relation[0]) + 1  # 1 ~ 8 최대 조합의 갯수는? 대충 254개 정도 된다.

    # 그렇다면 모든 조합을 따져볼까? 유일성을 만족하는지 그리고 최소성을 만족하는지 따져봐야한다.
    # 먼저 어떤 조합에서 유일성을 만족할려면 어떻게 할까?
    # 최소성을 만족시키는 방법... 이것도 자료구조 set을 사용하면 될까?
    candidate_key_list = []
    for i in range(1, total_column):
        candidate_key_list += list(combinations(range(total_column - 1), i))
    count = 0
    for idx, candidate_key in enumerate(candidate_key_list):
        if is_unique(relation, candidate_key):
            count += 1
            # 이것을 계속해서 반복 탐색하는 것은 비효율적인데...
            # 하... 여기서 Idx + 1을 안해줘서... idx 부터 해버려서... candidate_key_list안에서 candidate_key이녀석도 삭제되어
            # 바로 뒤의 녀석이 건너뛰어져 버리는 문제가 발생하네...
            for n_idx in reversed(range(idx + 1, len(candidate_key_list))):
                n_candidated_key = candidate_key_list[n_idx]
                if all(c in n_candidated_key for c in candidate_key):
                    candidate_key_list.pop(n_idx)
    return count
