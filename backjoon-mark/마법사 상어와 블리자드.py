def solution():
    def board_to_array():
        point = shark_point
        cycle_pattern = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        cycle = 1
        array = []
        zero_flag = False
        while not zero_flag:
            for i in range(4):
                if zero_flag:
                    break
                for _ in range(2 * cycle - (1 if i < 2 else 0)):
                    if zero_flag:
                        break
                    y, x = point
                    dy, dx = cycle_pattern[i]
                    point = (y + dy, x + dx)
                    array.append((point, bead_board[point[0]][point[1]]))
                    if point == (0, 0) or bead_board[point[0]][point[1]] == 0:
                        zero_flag = True
            cycle += 1
        return array

    def get_effected_points(d, s):
        direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
        dy, dx = direction[d]
        point = shark_point
        effected_points = []
        for i in range(1, s + 1):
            effected_points.append((point[0] + dy * i, point[1] + dx * i))
        return effected_points

    def remove_continuous_beads(*arrays):
        no_continuous = False
        arrays = list(*arrays)
        arrays.append(0)
        while not no_continuous:
            stack = []
            no_continuous = True
            for idx, bead in enumerate(arrays):
                if stack and arrays[stack[-1]] != bead:
                    if len(stack) >= 4:
                        no_continuous = False
                        prev_bead = arrays[stack[-1]]
                        bead_count[prev_bead] += len(stack)
                        while stack:
                            top_idx = stack.pop()
                            arrays[top_idx] = 0
                    else:
                        stack.clear()
                stack.append(idx)
            # 모든 반복되는 녀석들은 다 0으로 처리했으니까... 모두 삭제하자 그것보단... 0인 것을 제외하고 새롭게 만들어나갈까?
            new_array = []
            for element in arrays:
                if element == 0:
                    continue
                new_array.append(element)
            arrays = new_array
        return arrays

    def update_bead_group(arrays):
        # 좌표값은 필요없으니까 없앤다.
        stack = []
        arrays.append(0)
        updated_bead_array = []
        for num in arrays:
            if stack and stack[-1] != num:  # 여기에서 여전히... stack이 남은 경우를 고려 안했구나... tmp에 임의로 0하나 추가함.
                size = len(stack)
                bead_num = stack[-1]
                updated_bead_array.append(size)
                updated_bead_array.append(bead_num)
                stack.clear()
            stack.append(num)
        return updated_bead_array

    def array_to_board(arrays):
        # 자... 현재 가지고 있는 배열을 다시 board에 업데이트 해줘야 한다.
        point = shark_point
        cycle_pattern = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        cycle = 1
        board = [[0] * N for _ in range(N)]
        arr_idx = 0
        arr_size = len(arrays)
        stop = False
        while not stop:
            for i in range(4):
                if stop:
                    break
                for _ in range(2 * cycle - (1 if i < 2 else 0)):
                    y, x = point
                    dy, dx = cycle_pattern[i]
                    if not (0 <= y + dy < N and 0 <= x + dx < N) or arr_idx == arr_size:
                        stop = True
                        break
                    board[y + dy][x + dx] = arrays[arr_idx]
                    arr_idx += 1
                    point = (y + dy, x + dx)  # 변경된 포인트 업데이트 안해서 한참 해맸다...
            cycle += 1
        return board

    N, M = map(int, input().split())
    bead_board = [list(map(int, input().split())) for _ in range(N)]
    magic_infos = [list(map(int, input().split())) for _ in range(M)]
    bead_count = {1: 0, 2: 0, 3: 0}
    shark_point = (-1 + (N + 1) // 2, -1 + (N + 1) // 2)
    for di, si in magic_infos:
        bead_arrays = board_to_array()
        effected_points = get_effected_points(di, si)
        for point, bead in bead_arrays[::-1]:
            if point in effected_points:
                bead_arrays.remove((point, bead))
        removed_arrays = remove_continuous_beads(bead for _, bead in bead_arrays)
        updated_bead_arrays = update_bead_group(removed_arrays.copy())
        bead_board = array_to_board(updated_bead_arrays)
    print(1 * bead_count[1] + 2 * bead_count[2] + 3 * bead_count[3])

def solution2():
    # 구슬이 연속된 것을 판단하기 위한 자료구조가 필요하다
    # 연속된 구슬이 4개 이상이면 폭발이 일어나고 계속해서 줄어든다. 더 이상 폭발할 녀석이 없을때까지 계속 이루어진다.
    # 폭발 후에는 변화한다? 그룹에 해당하는 구슬들... 즉 4개 미만의 연속된 녀석들은 같은 녀석들이 2개로 변한다.
    # 구해야하는 것은 각 번호에 해당하는 구슬의 갯수
    def get_marble_array():
        def dfs(node, direct):
            if node == shark_point:
                return
            arr.append(board[node[0]][node[1]])
            board[node[0]][node[1]] = -1
            # 이제 다음 녀석을 탐색해 나가야 한다.
            n_node = (node[0] + dy[direct], node[1] + dx[direct])
            if not (0 <= n_node[0] < N and 0 <= n_node[1] < N and board[n_node[0]][n_node[1]] >= 0):
                direct = (direct + 1) % 4
                n_node = (node[0] + dy[direct], node[1] + dx[direct])
            dfs(n_node, direct)
            # 여기서 또 같은 direct로 탐색해 나가야 하는데... 어떤 조건으로 방향을 바꾸지? 다음 노드가 막다른 길이거나 구슬이 0이거나
        arr = []
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        dfs((0, 0), 0)
        return arr

    def remove_all_zero(array):
        while 0 in array:
            array.remove(0)

    def explode_4seq_marble(array):
        # 한 배열에서 연속적인 수가 4개 이상있으면 어떻게 삭제할까? 단순삭제가 아니라 연속된 삭제여야한다.
        new_array = array.copy()
        is_continue = True
        while is_continue:
            # 여기서 부터 계속 체크를 해나가면서 지워나가야 한다.
            stack = [] # 스택에는 결국 같은 녀석들만 채워질 것이다.
            # 근데 여기서... 폭발할 것이 없다는 것을 어떻게 체크할까?
            for i in range(len(new_array)):
                if stack and (new_array[stack[-1]] != new_array[i]):
                    if len(stack) >= 4:
                        seq_num = new_array[stack[-1]]
                        exploded_marble_count[seq_num] += len(stack)
                        # 그리고 0으로 바꿔야한다.
                        while stack:
                            idx = stack.pop()
                            new_array[idx] = 0
                    stack.clear()
                stack.append(i)
            # 이제 여기서 0으로 바뀐 녀석들을 지워야한다.
            if 0 not in new_array:
                is_continue = False
            remove_all_zero(new_array)
        return new_array

    def update(array):
        new_array = []
        stack = []  # 어쨋든 스택에는 같은 녀석들만 넣는다.
        for i in range(len(array)):
            if stack and array[stack[-1]] != array[i]:
                # 스택에 새로운 녀석을 넣어야하는 때가 오면... 업데이트를 해야지?
                new_array.append(len(stack))
                new_array.append(array[stack[-1]])
                stack.clear()
            stack.append(i)
        return new_array



    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    skills = [list(map(int, input().split())) for _ in range(M)]
    shark_point = (N // 2, N // 2)
    exploded_marble_count = {i: 0 for i in range(1, 4)}
    skill_direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    # 특정 좌표에 어떤 구슬이 있는지는 board 을 사용하면 되겠고... 이 회전을 어떻게 처리하지...?
    for skill in skills:
        direction, distance = skill
        # 공격을 받은 좌표의 구슬은 0으로 처리한다.
        for i in range(1, distance + 1):
            n_y = shark_point[0] + (skill_direction[direction][0] * i)
            n_x = shark_point[1] + (skill_direction[direction][1] * i)
            board[n_y][n_x] = 0
        # 모든 좌표에 대해서 스택으로 처리하고...
        marble_array = get_marble_array()
        print(marble_array)
        remove_all_zero(marble_array)
        print(marble_array)
        exploded_marble = explode_4seq_marble(marble_array)
        print(exploded_marble)
        updated_marble = update(exploded_marble)
        print(updated_marble)
        # board = update_board(marble_array)
        # 자 여기서 array 을 돌면서 좌표 하나하나당 확인을 하고 그 값이 0 이면 삭제를 시킨다.
        # 그리고 4개 이상인 녀석이 있는지 확인하고 폭발을 일으킨다. 이건 계속 반복되어야한다. 그리고 기록을 한다.
        # 자 이제 marble 여기는 업데이트를 해줘야한다...
        # 아... 이러면 스택에다가 좌표를 기록하는 것이 맞나...?좌표를 기록할게 아니라... 구슬번호를 모두 집어넣고, 0이면 삭제를 해버리고 4개 연속되면 폭발시키고
        # 폭발 다 끝나면 업데이트하고 다시 board 에 써내려간다. 이게 맞는것같다.

bead_1, bead_2, bead_3 = 0, 0, 0
def solution3():
    global bead_1, bead_2, bead_3

    def execute_skill(d, s):
        dy, dx = direction[d]
        broken_beads = []
        for ds in range(1, s + 1):
            broken_beads.append((m_y + ds * dy, m_x + ds * dx))
        return broken_beads

    def move_and_explode(broken_beads):
        global bead_1, bead_2, bead_3

        # 자 여기서 회전하는 board에 대해서 스택을 만들어야하는데....
        spin_direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        spin_step = 0
        spin_point = 0
        n_y, n_x = m_y, m_x
        flag = True
        stack = []
        while flag:
            dy, dx = spin_direction[spin_point % 4]
            next_step = spin_step // 2 + 1
            for i in range(1, next_step + 1):
                n_y, n_x = n_y + dy, n_x + dx
                if board[n_y][n_x] == 0 or (n_y, n_x) == (0, 0):
                    flag = False
                    break
                if (n_y, n_x) not in broken_beads:
                    stack.append(board[n_y][n_x])
            spin_point += 1
            spin_step += 1
        # 자 이제 파괴된 후 배열을 구했으니... 폭발을 하자.
        while 1:
            exploded_beads = get_seq_beads(stack)
            if len(exploded_beads) == len(stack):
                break
            stack = exploded_beads
        return stack

    # 이코드... gpt도 별로였는데 내가짠 이게 훨씬 나은거 같다
    def get_seq_beads(beads):
        global bead_1, bead_2, bead_3

        stack = []
        i = 0
        while i < len(beads):
            count = 1
            while i + count < len(beads) and beads[i] == beads[i + count]:
                count += 1
            if count < 4:
                stack += beads[i:i + count]
            else:  # 카운팅 할 것이 아니면 이건 필요없지
                if beads[i] == 1:
                    bead_1 += count
                elif beads[i] == 2:
                    bead_2 += count
                elif beads[i] == 3:
                    bead_3 += count
            i += count
        return stack

    def update_board(beads):
        # 이제 bead을 변화시키자.
        stack = []
        i = 0
        while i < len(beads):
            count = 1
            while i + count < len(beads) and beads[i] == beads[i + count]:
                count += 1
            stack += [count, beads[i]]
            i += count

        # 이제 변화된 구슬들을 board에 넣어야한다.
        spin_direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        spin_step = 0
        spin_point = 0
        n_y, n_x = m_y, m_x
        flag = True
        stack = stack[::-1]
        while flag:
            dy, dx = spin_direction[spin_point % 4]
            next_step = spin_step // 2 + 1
            for i in range(1, next_step + 1):
                n_y, n_x = n_y + dy, n_x + dx
                if stack:
                    board[n_y][n_x] = stack.pop()
                else:
                    board[n_y][n_x] = 0
                if (n_y, n_x) == (0, 0):
                    flag = False
                    break
            spin_point += 1
            spin_step += 1

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    skills = [list(map(int, input().split())) for _ in range(M)]
    direction = {1:(-1, 0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}
    m_y, m_x = ((N + 1) // 2) - 1, ((N + 1) // 2) - 1

    for d, s in skills:
        broken_beads = execute_skill(d, s)
        new_bead_array = move_and_explode(broken_beads)
        update_board(new_bead_array)

    print(1 * bead_1 + 2 * bead_2 + 3 * bead_3)


    pass
solution3()
