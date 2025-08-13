def solution():
    import copy
    
    # 함수에서 테이블 전체를 들고다니기는 너무 빡센데... 근데 뭐 엄청 큰건 아니긴 하지만... 해봤자 20짜리 3줄? 어 할만한가?
    # 안들고다닌다면.. 계속 넣었다 뺏다 반복해야하는데 그걸 어케하지? 음 그걸 역시 풀어야하나? 재귀호출 이전상태를 만들어주는것...
    # 왔던 길을 가면안된다 이걸 막아줘야 하는데...
    def move(tables, path: list):
        if len(tables[2]) == N: # 종료조건은 나중에 바꿀것이다.
            paths.append(path.copy()) # 재귀를 나와서 path 에 변경이 생기면.. 안에 녀석까지 바뀔수있지
            return
        for c_table_idx in [0, 1, 2]:
            if not tables[c_table_idx]:
                continue
            for n_table_idx in [0, 1, 2]:
                if c_table_idx == n_table_idx:
                    continue
                # 옮겨갈 곳이 비었다면 그냥 옮긴다.
                if not tables[n_table_idx] or tables[n_table_idx][-1] > tables[c_table_idx][-1]:
                    tmp_tables = copy.deepcopy(tables)
                    tmp_tables[n_table_idx].append(tmp_tables[c_table_idx].pop())
                    tmp_path = path.copy()
                    tmp_path.append((c_table_idx, n_table_idx))
                    move(tmp_tables, tmp_path)
                    
    N = int(input())
    lst = [[] for _ in range(3)]
    lst[0] = [i for i in range(N, 0, -1)]   
    paths = []
    move(lst, [])
    print(paths)
    
def solution2():
    N = int(input())
    def hanoi(n, start, via, end):
        if n == 1: # 원반의 갯수가 1개라면
            print(start, end)
        else:
            hanoi(n - 1, start, end, via)
            print(start, end)
            hanoi(n - 1, via, start, end)
    
    print(2**N - 1)
    hanoi(N, 1, 2, 3)
    #A -> C로 n개의 원판을 옮기려면
    # 1. A -> B로 n-1개의 원판을 옮기고,
    # 2. A -> C로 가장 큰 원판을 옮기고,
    # 3. B -> C로 n-1개의 원판을 옮겨야한다.
        
solution2()