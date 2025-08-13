def solutiuon():
    from collections import defaultdict
    
    n = int(input())
    infos = [tuple(input().split()) for _ in range(n)]
    # 현재 회사에 있는 모든 사람의 이름을 출력해야 하는 구나
    current_state = defaultdict(str)
    for name, state in infos:
        current_state[name] = state
    for name in sorted(list(current_state), reverse=True):
        if current_state[name] == "enter":
            print(name)


solutiuon()