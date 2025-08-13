def solution(uid, bid):
    def check_matching(a, b):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if b[i] == "*":
                continue
            if a[i] != b[i]:
                return False
        return True
    
    def dfs(user_ids, banned_user_ids, user_checked, ban_checked, count):
        # 하 이게 탐색만 끝났지 경우의 수는 아니잖아... 매칭된거 없이.. 그냥 다 돌았어도 체크가 되는거네
        if user_checked == (1 << len(uid)) - 1 or ban_checked == (1 << len(bid)) -1:
            count += 1
            return count
        
        for i, user_id in enumerate(user_ids):
            if (user_checked & 1 << i) != 0: 
                continue
            for j, banned_user_id in enumerate(banned_user_ids):
                if (ban_checked & 1 << j) != 0:
                    continue
                if check_matching(user_id, banned_user_id):
                    count = max(count, dfs(user_ids, banned_user_ids, user_checked ^ 1 << i, ban_checked ^ 1 << j, count)) 
            user_checked = user_checked ^ 1 << i 
        return count
    
    user_checked = 0b0 # 비트마스킹으로 체크했다는 것을 마킹해두자.
    ban_checked = 0b0
    return dfs(uid, bid, user_checked, ban_checked, 0)
    
def solution2(u_ids, b_ids):
    def check_matching(a, b):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if b[i] == "*":
                continue
            if a[i] != b[i]:
                return False
        return True
    
    
    def dfs(user_ids:list, ban_user_ids:list, path:list):
        if not ban_user_ids:
            path.sort()
            answers.add(tuple(path))
        
        for i, user_id in enumerate(user_ids):
            for j, ban_user_id in enumerate(ban_user_ids):
                if check_matching(user_id, ban_user_id):
                    tmp_path = path.copy()
                    tmp_path.append(user_id)
                    dfs(user_ids[i+1:] if i + 1 < len(user_ids) else [],
                        ban_user_ids[:j] + (ban_user_ids[j+1:] if j + 1 < len(ban_user_ids) else []),
                        tmp_path)
    
    answers = set()
    dfs(u_ids, b_ids, [])
    print(answers)
    return len(answers)

print(solution2(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))


def solution(u_ids, b_ids):
    def check(uid, bid):
        if len(uid) != len(bid):
            return False
        for i in range(len(uid)):
            if uid[i] != bid[i]:
                if bid[i] == "*":
                    continue
                return False
        return True

    def dfs(user_ids, banned_ids, path):
        if len(path) == len(b_ids):
            path.sort()
            results.add(tuple(path))

        for banned_id in banned_ids:
            for idx, user_id in enumerate(user_ids):
                if check(user_id, banned_id):
                    next_path = path.copy()
                    next_path.append(user_id)
                    # remain_user_ids = user_ids.copy()
                    # remain_user_ids.remove(user_id)  여기 부분... 생각하기 쉽지 않았다.
                    remain_banned_ids = banned_ids.copy()
                    remain_banned_ids.remove(banned_id)
                    dfs(user_ids[idx + 1:] if idx + 1 < len(user_ids) else [], remain_banned_ids, next_path)

    results = set()
    dfs(u_ids, b_ids, [])
    return len(results)


def solution(u_ids, b_ids):
    from collections import defaultdict
    from itertools import product, combinations, permutations

    def check(uid, bid):
        if len(uid) != len(bid):
            return False
        for i in range(len(uid)):
            if uid[i] != bid[i]:
                if bid[i] == "*":
                    continue
                return False
        return True

    def dfs(node, path):
        if len(path) == len(b_ids):
            path.sort()
            results.add(tuple(path))
            return

        for next_node in candidates[node]:
            if next_node in path:
                continue
            next_path = path.copy()
            next_path.append(next_node)
            dfs(node + 1, next_path)

    candidates = defaultdict(list)
    for idx, banned_id in enumerate(b_ids):
        for user_id in u_ids:
            if check(user_id, banned_id):
                candidates[idx].append(user_id)
    print(candidates)
    # 자 여기서 한쪽 리스트에서 하나씩 뽑아내는 조합을 구해야한다.
    results = set()
    dfs(0, [])
    print(results)
    return len(results)


def solution2(user_id_lst, banned_id_lst):
    def match(banned_id, user_id):
        # 어쨋든 각 아이디의 길이는 최대 8이다.
        if len(banned_id) != len(user_id):
            return False
        for i in range(len(banned_id)):
            if banned_id[i] == "*":
                continue
            if banned_id[i] != user_id[i]:
                return False
        return True

    def check_lst(banned_ids, user_ids):
        # 2개의 리스트가 매칭되냐 안되냐?

        N = len(banned_ids)
        for i in range(N):
            banned_id = banned_ids[i]
            user_id = user_ids[i]
            if not match(banned_id, user_id):
                return False
        return True
    from itertools import combinations, permutations

    # 몇가지 경우의 수가 가능한지 리턴해야한다.
    # 하나의 banned_id에 *은 1개 이상 있을 수 있다.

    answer = 0
    for user_ids in combinations(user_id_lst, len(banned_id_lst)):  # 이거 최대 70임
        for user_ids_ in permutations(user_ids, len(user_ids)):
            if check_lst(banned_id_lst, user_ids_):
                answer += 1
                break
    return answer