def solution(lottos, win_nums):
    win_count = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    zero_count = lottos.count(0)
    lottos = set(lottos)
    win_nums = set(win_nums)
    cha_set = win_nums - lottos
    prev_matching_count = len(win_nums) - len(cha_set)
    max_matching_count = prev_matching_count + (len(cha_set) if zero_count >= len(cha_set) else zero_count)
    
    return [win_count[max_matching_count], win_count[prev_matching_count]]


print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))

# 시간복잡도를 고려안하고 풀었더니... 시간초과가 걸렸다. 최대 800만의 조합이 나올 수 있고... 하나당 6개니까... 4800만...
# 거기다 조합을 구하는 과정도 어마어마할 것이다.