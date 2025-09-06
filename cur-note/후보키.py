from collections import deque
from itertools import combinations

def solution(relation):
    col_size = len(relation[0])
    row_size = len(relation)
    
    # 크기 1부터 모든 가능한 키 조합을 생성
    possible_keys = deque()
    for i in range(1, col_size + 1):
        # combinations를 쓰면 자동으로 크기 순으로 정렬된 효과를 봅니다.
        for combo in combinations(range(col_size), i):
            possible_keys.append(set(combo))

    # 최종 후보키를 담을 리스트
    result_keys = []
    while possible_keys:
        possible_key = possible_keys.popleft()
        
        # 확정된 후보키가 현재의 possible_key의 부분집합이면 건너뛴다.
        is_minimal = True
        for candidate_key in result_keys:
            if candidate_key.issubset(possible_key):
                is_minimal = False
                break
        if not is_minimal:
            continue
        
        db_set = set()
        is_unique = True
        for row in relation:
            sub_tuple = tuple(row[idx] for idx in possible_key)
            if sub_tuple in db_set:
                is_unique = False
                break
            db_set.add(sub_tuple)
        # key가 후보키로 만족된다면
        if is_unique:
            result_keys.append(possible_key)
    return len(result_keys)
    
    