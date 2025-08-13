def unlock(window, lock):
    # 하나 유의할 것은 여기서 lock의 값을 바꾼다면 이 함수를 호출한 check의 lock도 값이 바뀐다.
    for i in range(len(window)):
        if lock[i] == 0 and window[i] != 1:
            return False
        elif lock[i] == 1 and window[i] == 1:
            return False
    return True

def check(key, lock):
    # 슬라이딩 윈도우로 가보자. 필요 없는 부분은 -1으로 처리하고
    filled_key = [-1] * len(lock) + key + [-1] * len(lock)
    lock_len = len(lock)
    print("filled_key", filled_key)
    for i in range(len(filled_key) - lock_len):
        window_key = filled_key[i:i + lock_len] # lock의 길이와 일치할 것이다.
        print(window_key)
        if unlock(window_key, lock):
            return True
    return False

def solution(key, lock):
    M = len(key)  # M은 항상 N이하
    N = len(lock)
    # 확실한 것은 회전하는데 있어서 1차원으로 푼것은 틀리지 않았다.
    key1 = [key[i][j] for i in range(M) for j in range(M)]
    key2 = [key[i][j] for j in range(M) for i in reversed(range(M))]
    key3 = key1[::-1]
    key4 = key2[::-1]
    plat_lock = [lock[i][j] for i in range(N) for j in range(N)]
    if check(key1, plat_lock) or check(key2, plat_lock) or check(key3, plat_lock) or check(key4, plat_lock):
        return True
    return False

print(solution([[0, 0], [0, 0]], [[1, 0, 0], [1, 0, 0], [1, 1, 1]]))



# 위의 코드는 완전 잘못된 풀이다. 그렇지만... 2차원을 1차원으로 바꾼 이러한 방법은 면밀히 살펴보아야한다.

def expand(key, n):
    # key의 상하좌우로 n만큼 확장시킨다. 값은 0으로
    expanded_len = n + len(key) + n
    expanded_key = [[0] * expanded_len for _ in range(expanded_len)]
    for i in range(expanded_len):
        for j in range(expanded_len):
            if n <= i < n + len(key) and n <= j < n + len(key):
                expanded_key[i][j] = key[i - n][j - n]
    return expanded_key


def rotate_90(key):
    return [col[::-1] for col in zip(*key)]


def unlock(key, lock):
    N = len(key)
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0 and key[i][j] != 1:
                return False
            elif lock[i][j] == 1 and key[i][j] == 1:
                return False
    return True


def check(key, lock):
    expanded_key = expand(key, len(lock))
    ex_len = len(expanded_key)
    # 자 이제부터 lock을 움직이며 체크한다.
    # lock을 움직이기보단 확장된 key을 잘라내는 것이 맞지 않나?
    key_window = []
    for i in range(ex_len - len(lock)):
        for j in range(ex_len - len(lock)):
            key_window = [expanded_key[k][j:j + len(lock)] for k in range(i, i + len(lock))]
            if unlock(key_window, lock.copy()):
                return True
    return False


def solution(key, lock):
    M = len(key)  # M은 항상 N이하
    N = len(lock)
    key_lst = [key]
    for _ in range(3):
        rotated_key = rotate_90(key)
        key_lst.append(rotated_key)
        key = rotated_key

    for rotated_key in key_lst:
        if check(rotated_key, lock):
            return True
    return False
